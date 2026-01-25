
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

cam_centre = (52.2053, 0.1218)
stations = build_station_list()


oneb = stations_by_distance(stations,cam_centre, True)

print("Closest 10 stations:", oneb[:10])
print("Furthest 10 stations:", oneb[-10:])