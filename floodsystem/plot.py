import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    """displays a plot of the water level data against time for a station, includes lines for the typical low and high levels"""

    # plots
    plt.plot(dates,levels)

    #adds labels and title
    plt.title(station.name)
    plt.xlabel("date")
    plt.ylabel("water level")

    #subplot lines 
    plt.axhline(y=station.typical_range[0], color='green', linestyle='--', label="Typical Low")
    plt.axhline(y=station.typical_range[1], color='red',   linestyle='--', label="Typical High")

    plt.xticks(rotation=45)
    plt.tight_layout()


    plt.show()