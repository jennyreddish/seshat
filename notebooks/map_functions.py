import geopandas as gpd
import folium
import folium
import ipywidgets as widgets
from IPython.display import display, clear_output
from distinctipy import get_colors, get_hex


def vectorized_convert_name(gdf):
    """
    Corrected vectorized version of convert_name to process the entire DataFrame at once.
    """
    # Remove parentheses from 'Name' and 'MemberOf'
    gdf['CleanName'] = gdf['Name'].str.replace('[()]', '', regex=True)
    gdf['CleanMember_of'] = gdf['MemberOf'].str.replace('[()]', '', regex=True)

    # Initialize DisplayName and ColorKey
    gdf['DisplayName'] = gdf['CleanName']
    gdf['ColorKey'] = gdf['CleanName']

    # Conditions for setting DisplayName to None
    # If the shape has components, is not a personal union, and the components don't have components
    has_components = gdf['Components'].notna() & gdf['Components'].str.len() > 0
    not_personal_union = ~gdf['SeshatID'].str.contains(';')
    components_without_components = ~gdf['Components'].str.contains('\\(')
    gdf.loc[has_components & not_personal_union & components_without_components, 'DisplayName'] = None

    # Correct Update ColorKey for shapes that are components of another shape
    gdf.loc[gdf['MemberOf'].notna() & gdf['MemberOf'].str.len() > 0, 'ColorKey'] = gdf['CleanMember_of']

    # Add type prefix to DisplayName where type is not 'POLITY'
    gdf.loc[gdf['Type'] != 'POLITY', 'DisplayName'] = gdf['Type'] + ': ' + gdf['DisplayName']

def cliopatria_gdf(cliopatria_geojson_path):
    """
    Load the Cliopatria shape dataset with GeoPandas, process names and colors efficiently.
    """
    gdf = gpd.read_file(cliopatria_geojson_path)

    # Apply vectorized name conversion
    vectorized_convert_name(gdf)

    # Use DistinctiPy package to assign a colour based on the ColorKey field
    colour_keys = gdf['ColorKey'].unique()
    colours = [get_hex(col) for col in get_colors(len(colour_keys))]
    colour_mapping = dict(zip(colour_keys, colours))

    # Map colors to a new column efficiently
    gdf['Color'] = gdf['ColorKey'].map(colour_mapping)

    # Drop intermediate columns
    gdf.drop(['CleanName', 'CleanMember_of'], axis=1, inplace=True)

    return gdf


def create_map(selected_year, gdf, map_output):
    global m
    m = folium.Map(location=[0, 0], zoom_start=2, tiles='https://a.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png', attr='CartoDB')

    # Filter the gdf for shapes that overlap with the selected_year
    filtered_gdf = gdf[(gdf['FromYear'] <= selected_year) & (gdf['ToYear'] >= selected_year)]

    # Filter the gdf for shapes where the personal unions etc is already plotted
    dontPlotMeBecauseImInAUnion = []
    def process_seshat_id(row):
        if ';' in row['SeshatID']:
            these_seshat_ids = row['SeshatID'].split(';')
            dontPlotMeBecauseImInAUnion.extend(these_seshat_ids)
    filtered_gdf.apply(process_seshat_id, axis=1)

    # Transform the CRS of the GeoDataFrame to WGS84 (EPSG:4326)
    filtered_gdf = filtered_gdf.to_crs(epsg=4326)

    # Define a function for the style_function parameter
    def style_function(feature, color):
        return {
            'fillColor': color,
            'color': color,
            'weight': 2,
            'fillOpacity': 0.5
        }

    # Add the polygons to the map
    for _, row in filtered_gdf.iterrows():
        # Ignore rows where the DisplayName is None
        if row['DisplayName'] is None or row['SeshatID'] in dontPlotMeBecauseImInAUnion:
            continue
        # Convert the geometry to GeoJSON
        geojson = folium.GeoJson(
            row.geometry,
            style_function=lambda feature, color=row['Color']: style_function(feature, color)
        )

        # Add a popup to the GeoJSON
        folium.Popup(row['DisplayName']).add_to(geojson)

        # Add the GeoJSON to the map
        geojson.add_to(m)

    # Display the map
    with map_output:
        clear_output(wait=True)
        display(m)


def display_map(gdf, display_year):

    # Create a text box for input
    year_input = widgets.IntText(
        value=display_year,
        description='Year:',
    )

    # Define a function to be called when the value of the text box changes
    def on_value_change(change):
        create_map(change['new'], gdf, map_output)

    # Create a slider for input
    year_slider = widgets.IntSlider(
        value=display_year,
        min=gdf['FromYear'].min(),
        max=gdf['ToYear'].max(),
        description='Year:',
    )

    # Link the text box and the slider
    widgets.jslink((year_input, 'value'), (year_slider, 'value'))

    # Create an output widget
    map_output = widgets.Output()

    # Attach the function to the text box
    year_input.observe(on_value_change, names='value')

    # Display the widgets
    display(year_input, year_slider, map_output)

    # Call create_map initially to display the map
    create_map(display_year, gdf, map_output)