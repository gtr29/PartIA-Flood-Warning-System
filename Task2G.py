from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
import datetime
import numpy as np


"""   following is a program that assesses the severity of the risk at each station, 
-based on data such as the relative/true water level,gradient of least squares polynomial etc. - 
and returns a list of the stations with the highest risk. 
Categorised into the following risk levels: Severe, High, Moderate, Low   """


stations = build_station_list()
update_water_levels(stations)

#empty list that holds all tuples

w1 = 1.5
w2 = 2
p = 4
dt = 2

def calculate_risk(dates, d0, w1, w2, station, poly):

    rel_level = station.relative_water_level()
    if rel_level is None:
        return 0.0  # filters out unavailable data
    
    if rel_level <= 0.8:
        score = 1
    
    else:
        derivative = np.polyder(poly)
        time = (dates[-1] - d0).total_seconds() / 86400.0
        gradient = derivative(time)

        score = (w1 * rel_level) + (w2 * gradient)

    return score


def assess_risk(w1,w2,p,stations):
    """ 
    aim to create a formula that returns a number 0-10 based on severity of flood, 10 being most sever 
    - any scores over 10 automatically get categorised as severe risk
    """

    station_risk = []
   
#python3 Task2G.py

    for station in stations:

        rel_level = station.relative_water_level()

        # skips stations with no dates 
        if rel_level is None:
            continue 

        #if water level is low (less than 80%) it is just recorded as LOW and skips derivative etc.
        if rel_level < 0.8:
            station_risk.append((station.name , "low" , rel_level))
            continue 


        # now analysing higher risk stations 
        print("analysing higher risk station:" + station.name)
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) == 0 or len(levels) == 0:
            continue
        
        # skipping missing datum
        if len(dates) == 0 or len(levels) == 0:
            continue

        poly, d0 = polyfit(dates, levels, p)
        
        #running calculation
        flood_risk = calculate_risk(dates, d0, w1, w2, station, poly)

        if flood_risk >= 8:
            risk = "severe"
        
        elif flood_risk >= 5:
            risk = "high"

        elif flood_risk >= 3:
            risk = "moderate"

        else:
            risk = "low"

        category = (station.name , risk, flood_risk)
        
        station_risk.append(category)

    station_risk.sort(key=lambda x: x[2], reverse=True)

    return station_risk

risky_stations = assess_risk(w1,w2,p,stations)

print(risky_stations[:20])
    