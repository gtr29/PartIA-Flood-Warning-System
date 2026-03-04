# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d


    def typical_range_consistent(self):
        # Check if data is missing (inconsistent)
        if self.typical_range is None:
            return False
            
        # Access individual values
        low = self.typical_range[0]
        high = self.typical_range[1]
        
        # Check if high is less than low (inconsistent)
        if high < low:
            return False
            
        # If both checks pass, it's consistent
        return True


    def relative_water_level(self):
        """Returns the latest water level as a fraction of the typical range, where 0 corresponds to the typical low and 1 corresponds to the typical high. If the data is inconsistent or unavailable, returns None."""
        if self.typical_range is None:
            return None
        if self.latest_level is None:
            return None
        if self.typical_range_consistent() == False:
            return None
        low = self.typical_range[0]
        high = self.typical_range[1]
        return (self.latest_level - low) / (high - low)
        

    



def inconsistent_typical_range_stations(stations):
    #empty list to hold failed stations
    failedStations = []

    #iterating through all stations
    for station in stations:
        if station.typical_range_consistent() == False:
            failedStations.append(station)

    return failedStations