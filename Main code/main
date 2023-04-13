import pyproj
from shapely.geometry import Polygon, Point
from shapely.ops import transform
from functools import partial
import icloud
import time
import datetime
active_location = icloud.location

def checker(point):
    #make sure to reverse coordinate before using this function.
    '''tuple --> bool
    uses a given point and dtermines t/f if present within map'''

    #projection onto earth
    project = partial(
        pyproj.transform,
        pyproj.Proj(init='epsg:4326'),
        pyproj.Proj('+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs'))

    #data points
    custom_map_coordinates =([-75.6647152, 45.4101448], 
                        [-75.6603704, 45.4130058], 
                        [-75.6624518, 45.4134879], 
                        [-75.6671296, 45.4128703], 
                        [-75.6696401, 45.4165606], 
                        [-75.6820856, 45.4209134], 
                        [-75.6829868, 45.4210941], 
                        [-75.6835447, 45.4205519], 
                        [-75.6829868, 45.4201905], 
                        [-75.6716142, 45.4154008], 
                        [-75.6697689, 45.412569], 
                        [-75.6647152, 45.4101448])
    custom_map_polygon = Polygon(custom_map_coordinates)
    active_location = Point(point)

    #reverse our polygon coordinates
    for i in range(len(custom_map_coordinates)):
        custom_map_coordinates[i].reverse()

    #transform points to project
    custom_map_polygon_transformed = transform(project, custom_map_polygon)
    active_location_transformed = transform(project, active_location)

    
    return custom_map_polygon_transformed.contains(active_location_transformed)


while True:
    active_location = icloud.location
    in_custom_map = checker(active_location)
    print(active_location)
    print(in_custom_map)
    if in_custom_map == True:
        pass
    else:
        print("nope")
    time.sleep(5)
