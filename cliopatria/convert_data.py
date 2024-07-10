import geopandas as gpd
from distinctipy import get_colors, get_hex
import sys

def cliopatria_gdf(gdf):
    """
    Load the Cliopatria shape dataset with GeoPandas, process names and colors efficiently.
    """

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


# Check if a GeoJSON file path was provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide the path to the GeoJSON file as a command line argument.")
    sys.exit(1)

geojson_path = sys.argv[1]

try:
    gdf = gpd.read_file(geojson_path)
except Exception as e:
    print(f"Error loading GeoJSON file: {str(e)}")
    sys.exit(1)

# Call the cliopatria_gdf function to process the GeoDataFrame
processed_gdf = cliopatria_gdf(gdf)

# Save the processed GeoDataFrame as a new GeoJSON file
output_path = geojson_path.replace('.geojson', '_seshat_processed.geojson')
try:
    processed_gdf.to_file(output_path, driver='GeoJSON')
    print(f"Processed GeoDataFrame saved to: {output_path}")
except Exception as e:
    print(f"Error saving processed GeoDataFrame: {str(e)}")
    sys.exit(1)
