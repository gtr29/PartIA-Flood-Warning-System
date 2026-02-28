from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)


num = 10
twoc = stations_highest_rel_level(stations, num)
final = []
for i in range(len(twoc)):
    final.append((twoc[i][0].name, twoc[i][1]))
print(final)