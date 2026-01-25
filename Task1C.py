from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

cam_centre = (52.2053, 0.1218)
radius = 10
stations = build_station_list()

onec = stations_within_radius(stations, cam_centre, radius)

onecnames = []
for i in range(len(onec)):
    onecnames.append(onec[i].name)

onecnames.sort()
print(onecnames)
