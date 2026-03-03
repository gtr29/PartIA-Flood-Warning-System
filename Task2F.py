from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime


stations = build_station_list()
update_water_levels(stations)

dt = 2   
n = 5  
p = 4 

top_stations = stations_highest_rel_level(stations, n)

for i in range(n):
    station = top_stations[i][0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_level_with_fit(station, dates, levels, p)