# Gordonvale tests
# HMSC

import osmnx as ox, geopandas as gpd
ox.config(log_file=True, log_console=True, use_cache=True)
location_point = (-17.1010286,145.7753749)

# create network from point, inside bounding box of N, S, E, W each 750m from point
G2 = ox.graph_from_point(location_point, distance=5000, distance_type='bbox', network_type='drive')
G2 = ox.project_graph(G2)
fig, ax = ox.plot_graph(G2, node_size=30, node_color='#66cc66')



import osmnx as ox, geopandas as gpd
ox.config(log_file=True, log_console=True, use_cache=True)
location_point = (-17.1010286,145.7753749)
gdf = ox.buildings_from_point(point=location_point,distance=5000)
gdf_proj = ox.project_gdf(gdf)
bbox = ox.bbox_from_point(point=location_point, distance=5000, project_utm=True)
fig, ax = ox.plot_buildings(gdf_proj)


import osmnx as ox, geopandas as gpd
ox.config(log_file=True, log_console=True, use_cache=True)

place_names = ['Gordonvale, Queensland, Australia']
east_bay = ox.gdf_from_places(place_names)
ox.save_gdf_shapefile(east_bay)
east_bay = ox.project_gdf(east_bay)
fig, ax = ox.plot_shape(east_bay)


import osmnx as ox
ox.config(log_file=True, log_console=True, use_cache=True)
city = ox.gdf_from_place('Sydney, New South Wales, Australia')
city
ox.save_gdf_shapefile(city)
city = ox.project_gdf(city)
fig, ax = ox.plot_shape(city)



import osmnx as ox
from IPython.display import Image
ox.config(log_console=True, use_cache=True)

# configure the inline image display
img_folder = 'images'
extension = 'png'
size = 240

# helper funcion to get one-square-mile street networks, building footprints, and plot them
def make_plot(place, point, network_type='drive', bldg_color='orange', dpi=40,
              dist=805, default_width=4, street_widths=None):
    gdf = ox.buildings_from_point(point=point, distance=dist)
    gdf_proj = ox.project_gdf(gdf)
    fig, ax = ox.plot_figure_ground(point=point, dist=dist, network_type=network_type, default_width=default_width,
                                    street_widths=street_widths, save=False, show=False, close=True)
    fig, ax = ox.plot_buildings(gdf_proj, fig=fig, ax=ax, color=bldg_color, set_bounds=False,
                                save=True, show=False, close=True, filename=place, dpi=dpi)


place = 'portland_buildings'
point = (45.517309, -122.682138)
make_plot(place, point)
Image('{}/{}.{}'.format(img_folder, place, extension), height=size, width=size)
