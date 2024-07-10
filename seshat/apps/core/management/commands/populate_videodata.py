import os
import json
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from django.db import connection
from seshat.apps.core.models import VideoShapefile


class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('geojson_file', type=str, help='Path to the geojson file')

    def handle(self, *args, **options):

        # TODO: change this to use JSON instead of GeoPandas
        # Load the Cliopatria shape dataset with GeoPandas
        cliopatria_geojson_path = options['geojson_file']
        self.stdout.write(self.style.SUCCESS(f"Loading Cliopatria shape dataset from {cliopatria_geojson_path}..."))
        gdf = gpd.read_file(cliopatria_geojson_path)
        self.stdout.write(self.style.SUCCESS(f"Successfully loaded Cliopatria shape dataset from {cliopatria_geojson_path}"))

        # Clear the VideoShapefile table
        self.stdout.write(self.style.SUCCESS('Clearing VideoShapefile table...'))
        VideoShapefile.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('VideoShapefile table cleared'))

        self.stdout.write(self.style.SUCCESS(f"Generating shape names and colors..."))
        gdf = cliopatria_gdf(gdf)

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

        self.stdout.write(self.style.SUCCESS(f"Successfully imported all data from {os.path.basename(geojson_file)}"))

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

