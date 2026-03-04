import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
import numpy as np 
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




def plot_water_level_with_fit(station, dates, levels, p):
    """Plots water level data and a best-fit polynomial of degree p."""

    poly, d0 = polyfit(dates, levels, p)

    # Convert dates to numbers
    t = []
    for d in dates:
        days_since_start = (d - d0).days
        t.append(days_since_start)
    t = np.array(t, dtype=float)

    plt.figure()
    plt.plot(dates, levels, label="Water Level")

    # Plot the polynomial fit
    plt.plot(dates, poly(t), color='purple', linestyle='--', label = ("degree:", p ))

    # Typical low and high lines
    plt.axhline(y=station.typical_range[0], color='green', linestyle='--', label="Typical Low")
    plt.axhline(y=station.typical_range[1], color='red',   linestyle='--', label="Typical High")

    plt.xlabel("Date")
    plt.ylabel("Water Level")
    plt.title(station.name)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(f"{station.name}_fit.png")
    plt.close()