from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
import datetime 
import matplotlib.pyplot as plt


stations = build_station_list()
update_water_levels(stations)

dt = 10
num = 5
twoc = stations_highest_rel_level(stations, num)

for i in range(num):
    station = twoc[i][0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_levels(station, dates, levels)
    plt.savefig(f"station_{i}.png")  
    plt.close()     