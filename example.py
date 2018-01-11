import osmnx as ox, geopandas as gpd
ox.config(log_file=True, log_console=True, use_cache=True)


city = ox.gdf_from_place('Manhattan, New York City, New York, USA')
ox.save_gdf_shapefile(city)
city = ox.project_gdf(city)
fig, ax = ox.plot_shape(city, figsize=(3,3))



import osmnx as ox, geopandas as gpd
ox.config(log_file=True, log_console=True, use_cache=True)

place_names = ['Berkeley, California, USA',
           'Oakland, California, USA',
           'Piedmont, California, USA',
           'Emeryville, California, USA',
           'Alameda, Alameda County, CA, USA']
east_bay = ox.gdf_from_places(place_names)
ox.save_gdf_shapefile(east_bay)
east_bay = ox.project_gdf(east_bay)
fig, ax = ox.plot_shape(east_bay)



import osmnx as ox, geopandas as gpd
ox.config(log_file=True, log_console=True, use_cache=True)
# define a bounding box in San Francisco
north, south, east, west = 37.79, 37.78, -122.41, -122.43

# create network from that bounding box
G1 = ox.graph_from_bbox(north, south, east, west, network_type='drive_service')
G1 = ox.project_graph(G1)
fig, ax = ox.plot_graph(G1)





import osmnx as ox, geopandas as gpd
ox.config(log_file=True, log_console=True, use_cache=True)
# define a point at the corner of California St and Mason St in SF
#location_point = (19.432608, -99.133209)
location_point = (-17.1010286,145.7753749)

# create network from point, inside bounding box of N, S, E, W each 750m from point
G2 = ox.graph_from_point(location_point, distance=5000, distance_type='bbox', network_type='drive')
G2 = ox.project_graph(G2)
fig, ax = ox.plot_graph(G2, node_size=30, node_color='#66cc66')

stats = ox.basic_stats(G2)
stats['circuity_avg']
