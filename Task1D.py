from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

stations = build_station_list()
partone = rivers_with_station(stations)
partone.sort()
print(len(partone),"stations, first 10 are:",partone[:10])


parttwo = stations_by_river(stations,True)
print(parttwo["River Aire"])
print(parttwo["River Cam"])
print(parttwo["River Thames"])