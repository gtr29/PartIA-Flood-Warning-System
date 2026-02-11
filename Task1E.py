from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list



stations = build_station_list()
print(rivers_by_station_number(stations, 9))
print(rivers_by_station_number(stations, 12))
