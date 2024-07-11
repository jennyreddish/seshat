import folium
import folium
import ipywidgets as widgets
from IPython.display import display, clear_output


def create_map(selected_year, gdf, map_output, components=False):
    global m
    m = folium.Map(location=[0, 0], zoom_start=2, tiles='https://a.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png', attr='CartoDB')

    # Filter the gdf for shapes that overlap with the selected_year
    filtered_gdf = gdf[(gdf['FromYear'] <= selected_year) & (gdf['ToYear'] >= selected_year)]

    if components:
        # Only shapes where the "Components" column is not populated (i.e., the shape doesn't have components, it is a lowest-level component itself)
        filtered_gdf = filtered_gdf[(filtered_gdf['Components'].isnull()) | (filtered_gdf['Components'] == '')]
    else:
        # Only shapes where the "MemberOf" column is not populated (i.e., the shape is not a member of another shape, it is a top-level shape itself)
        filtered_gdf = filtered_gdf[(filtered_gdf['MemberOf'].isnull()) | (filtered_gdf['MemberOf'] == '')]
        # Also filter out "Personal Union" composites where the SeshatId includes a semicolon to avoid overlaps
        filtered_gdf = filtered_gdf[~filtered_gdf['SeshatID'].str.contains(';')]

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

    # Create a slider for input
    year_slider = widgets.IntSlider(
        value=display_year,
        min=gdf['FromYear'].min(),
        max=gdf['ToYear'].max(),
        description='Year:',
    )

    # Link the text box and the slider
    widgets.jslink((year_input, 'value'), (year_slider, 'value'))

    # Create a radio button to switch between "Polities" and "Components".
    # The value should be a boolean indicating whether to display components or not.
    components_radio = widgets.RadioButtons(
        options=['Polities', 'Components'],
        description='Display:',
        disabled=False
    )

    # Define a function to be called when the value of the text box changes
    def on_value_change(change):
        if components_radio.value == 'Polities':
            create_map(change['new'], gdf, map_output)
        elif components_radio.value == 'Components':
            create_map(change['new'], gdf, map_output, components=True)

    # Define a function to be called when the value of the radio button changes
    def on_radio_change(change):
        if change['new'] == 'Polities':
            create_map(year_input.value, gdf, map_output)
        elif change['new'] == 'Components':
            create_map(year_input.value, gdf, map_output, components=True)

    # Attach the function to the text box
    year_input.observe(on_value_change, names='value')

    # Attach the function to the radio button
    components_radio.observe(on_radio_change, names='value')

    # Create an output widget
    map_output = widgets.Output()

    # Display the widgets
    display(year_input, year_slider, components_radio, map_output)

    # Call create_map initially to display the map
    create_map(display_year, gdf, map_output, )