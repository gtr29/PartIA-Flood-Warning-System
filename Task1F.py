from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list
inconsistent = inconsistent_typical_range_stations(stations)

sorted = []
for i in range(len(inconsistent)):
    sorted.append(sorted[i])

print(sorted.sort)