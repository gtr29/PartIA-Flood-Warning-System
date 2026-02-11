from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
inconsistent = inconsistent_typical_range_stations(stations)

sorted_Station_Names = []
for i in range(len(inconsistent)):
    sorted_Station_Names.append(inconsistent[i].name)

sorted_Station_Names.sort()
print(sorted_Station_Names)

