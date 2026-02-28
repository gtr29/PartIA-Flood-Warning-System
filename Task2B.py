from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)
tol = 0.8
twob = stations_level_over_threshold(stations, 0.8)
final = []
for i in range(len(twob)):
    final.append((twob[i][0].name, twob[i][1]))
print(final)
