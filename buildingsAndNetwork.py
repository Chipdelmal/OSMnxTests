################################################################################
# OSMnx tests
# Playing around with OSMnx
# HMSC
################################################################################

#Load package #################
import osmnx as ox, geopandas as gpd
ox.config(log_file=True, log_console=True, use_cache=True)
# Parameters ##################
location_point=(-17.1010286,145.7753749)    # Gordonvale
location_point=(-16,8122246,145.7183589)    # Yorkey's Knob
location_point=(-11.71654,43.42988)         # Comoros
distance=5000
# Roads #######################
G2 = ox.graph_from_point(location_point,distance=5000,distance_type='bbox',network_type='drive')
G2 = ox.project_graph(G2)
#fig, ax = ox.plot_graph(G2, node_size=30, node_color='#66cc66')
# Buildings ###################
gdf = ox.buildings_from_point(point=location_point,distance=distance)
gdf_proj = ox.project_gdf(gdf)
bbox = ox.bbox_from_point(point=location_point,distance=distance,project_utm=True)
fig, ax = ox.plot_buildings(gdf_proj,show=True)
