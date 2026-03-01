import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    """displays a plot of the water level data against time for a station, includes lines for the typical low and high levels"""

    plt.plot(dates,levels)
    plt.show()