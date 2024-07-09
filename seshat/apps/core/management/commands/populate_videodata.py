import os
import json
import geopandas as gpd
from distinctipy import get_colors, get_hex
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from django.db import connection
from seshat.apps.core.models import VideoShapefile


class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Directory containing geojson files')

    def handle(self, *args, **options):
        dir = options['dir']

        # Clear the VideoShapefile table
        self.stdout.write(self.style.SUCCESS('Clearing VideoShapefile table...'))
        VideoShapefile.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('VideoShapefile table cleared'))

        # Iterate over files in the directory
        for filename in os.listdir(dir):
            if filename.endswith('.geojson'):
                file_path = os.path.join(dir, filename)

        # Load the Cliopatria shape dataset with GeoPandas
        self.stdout.write(self.style.SUCCESS(f"Loading Cliopatria shape dataset from {file_path}"))
        gdf = cliopatria_gdf(file_path)

        self.stdout.write(self.style.SUCCESS('Adding data to the database...'))
        # Iterate through the GeoDataframe and create VideoShapefile instances
        for index, row in gdf.iterrows():
            self.stdout.write(self.style.SUCCESS(f"Creating VideoShapefile instance for {row['DisplayName']} ({row['FromYear']} - {row['ToYear']})"))
            
            # Save geom and convert Polygon to MultiPolygon if necessary
            geom = GEOSGeometry(json.dumps(row['geometry']))
            if geom.geom_type == 'Polygon':
                geom = MultiPolygon(geom)

            VideoShapefile.objects.create(
                geom=geom,
                name=row['DisplayName'],
                polity=row['ColorKey'],
                wikipedia_name=row['Wikipedia'],
                seshat_id=row['SeshatID'],
                area=row['Area'],
                start_year=row['FromYear'],
                end_year=row['ToYear'],
                polity_start_year=row['PolityStartYear'],
                polity_end_year=row['PolityEndYear'],
                colour=row['Color']
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully imported all data from {filename}"))

        ###########################################################
        ### Adjust the tolerance param of ST_Simplify as needed ###
        ###########################################################

        self.stdout.write(self.style.SUCCESS('Adding simplified geometries for faster loading...'))

        ## Use this code if you want to simplify the geometries
        # with connection.cursor() as cursor:
        #     cursor.execute("""
        #         UPDATE core_videoshapefile 
        #         SET simplified_geom = ST_Simplify(geom, 0.07);
        #     """)

        ## Use this code if you don't need to simplify the geometries
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE core_videoshapefile
                SET simplified_geom = geom;
            """)
        self.stdout.write(self.style.SUCCESS('Simplified geometries added'))


def cliopatria_gdf(cliopatria_geojson_path):
    """
    Load the Cliopatria shape dataset with GeoPandas, process names and colors efficiently.
    """
    gdf = gpd.read_file(cliopatria_geojson_path)

    self.stdout.write(self.style.SUCCESS(f"Generating shape names..."))

    # Remove parentheses from 'Name' and 'MemberOf'
    gdf['CleanName'] = gdf['Name'].str.replace('[()]', '', regex=True)
    gdf['CleanMember_of'] = gdf['MemberOf'].str.replace('[()]', '', regex=True)

    # Initialize DisplayName and ColorKey
    gdf['DisplayName'] = gdf['CleanName']
    gdf['ColorKey'] = gdf['CleanName']

    # Conditions for setting DisplayName to None: If the shape has components, is not a personal union, and the components don't have components
    has_components = gdf['Components'].notna() & gdf['Components'].str.len() > 0
    not_personal_union = ~gdf['SeshatID'].str.contains(';')
    components_without_components = ~gdf['Components'].str.contains('\\(')
    gdf.loc[has_components & not_personal_union & components_without_components, 'DisplayName'] = None

    # Correct Update ColorKey for shapes that are components of another shape
    gdf.loc[gdf['MemberOf'].notna() & gdf['MemberOf'].str.len() > 0, 'ColorKey'] = gdf['CleanMember_of']

    # Add type prefix to DisplayName where type is not 'POLITY'
    gdf.loc[gdf['Type'] != 'POLITY', 'DisplayName'] = gdf['Type'] + ': ' + gdf['DisplayName']

    self.stdout.write(self.style.SUCCESS(f"Generated shape names for {len(gdf)} shapes."))
    self.stdout.write(self.style.SUCCESS(f"Assigning colours to shapes..."))

    # Use DistinctiPy package to assign a colour based on the ColorKey field
    colour_keys = gdf['ColorKey'].unique()
    colours = [get_hex(col) for col in get_colors(len(colour_keys))]
    colour_mapping = dict(zip(colour_keys, colours))

    # Map colors to a new column efficiently
    gdf['Color'] = gdf['ColorKey'].map(colour_mapping)

    # Drop intermediate columns
    gdf.drop(['CleanName', 'CleanMember_of'], axis=1, inplace=True)

    self.stdout.write(self.style.SUCCESS(f"Assigned colours to {len(gdf)} shapes."))
    self.stdout.write(self.style.SUCCESS(f"Determing polity start and end years..."))

    # Add a column called 'PolityStartYear' to the GeoDataFrame which is the minimum 'FromYear' of all shapes with the same 'Name'
    gdf['PolityStartYear'] = gdf.groupby('Name')['FromYear'].transform('min')

    # Add a column called 'PolityEndYear' to the GeoDataFrame which is the maximum 'ToYear' of all shapes with the same 'Name'
    gdf['PolityEndYear'] = gdf.groupby('Name')['ToYear'].transform('max')

    self.stdout.write(self.style.SUCCESS(f"Determined polity start and end years for {len(gdf)} shapes."))

    return gdf
