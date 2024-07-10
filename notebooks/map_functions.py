import folium
import folium
import ipywidgets as widgets
from IPython.display import display, clear_output


def create_map(selected_year, gdf, map_output):
    global m
    m = folium.Map(location=[0, 0], zoom_start=2, tiles='https://a.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png', attr='CartoDB')

    # Filter the gdf for shapes that overlap with the selected_year
    filtered_gdf = gdf[(gdf['FromYear'] <= selected_year) & (gdf['ToYear'] >= selected_year)]

    # Filter the gdf for shapes where the personal unions etc is already plotted
    # This logic also exists in JavaScript in the plotPolities() function in the world_map.html
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