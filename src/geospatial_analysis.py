## `src/geospatial_analysis.py`
import pandas as pd
import geopandas as gpd
import folium
import os
import osmnx as ox
import networkx as nx

def generate_ev_map(csv_path='data/filtered_alt_fuel_stations.csv', output_html='data/all_ev_stations_map.html'):
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return
    
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=['latitude', 'longitude'])
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326"
    )
    
    ev_map = folium.Map(location=[32.7157, -117.1611], zoom_start=10)
    for _, row in gdf.iterrows():
        popup_text = f"""
        <b>Station Name:</b> {row['station_name']}<br>
        <b>Street Address:</b> {row['street_address']}<br>
        <b>City:</b> {row['city']}<br>
        <b>ZIP Code:</b> {row['zip']}<br>
        <b>Fuel Type:</b> {row['fuel_type_code']}<br>
        <b>EV Network:</b> {row['ev_network']}<br>
        """
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(ev_map)
    
    ev_map.save(output_html)
    print(f"EV map saved to {output_html}")

def calculate_route(sdge_location, ev_charger_location, distance=3000):
    G = ox.graph_from_point(sdge_location, dist=distance, network_type='drive')
    orig_node = ox.distance.nearest_nodes(G, sdge_location[1], sdge_location[0])
    dest_node = ox.distance.nearest_nodes(G, ev_charger_location[1], ev_charger_location[0])
    route = nx.shortest_path(G, orig_node, dest_node, weight='length')
    route_length = sum(ox.utils_graph.get_route_edge_attributes(G, route, 'length'))
    print(f"The driving distance from SDG&E to the selected EV charger is {route_length} meters.")
    fig, ax = ox.plot_graph_route(G, route, node_size=0)
