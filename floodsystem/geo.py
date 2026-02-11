# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine, Unit
from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p , minimise=False):
    """Takes a list of MonitoringStation objects, a coordinate p and optional parameter minimise, returns a list of (station, distance) tuples sorted by distance from p. Can be adjusted to output all station data or just name and town by assigning minimise as True."""
    stationdistance = []
    for i in range(len(stations)):
        distance = haversine(stations[i].coord, p)
        if minimise == False:
            stationdistance.append((stations[i], distance))
        else:
            stationdistance.append((stations[i].name, stations[i].town, distance))
    if minimise == False:
        return sorted_by_key(stationdistance, 1)
    else:
        return sorted_by_key(stationdistance, 2)


def stations_within_radius(stations, centre, r):
    """Takes a list of MonitoringStation objects, a coordinate centre and a radius. Returns a list of stations within radius from coordinate."""
    withinr = []
    for i in range(len(stations)):
        distance = haversine(stations[i].coord, centre)
        if distance <= r:
            withinr.append(stations[i])
    return withinr


def rivers_with_station(stations):
    """"Takes a list of MonitoringStation objects and returns a list of all rivers with a station."""
    rivers = set()
    for i in range(len(stations)):
        rivers.add(stations[i].river)
    riverslist = list(rivers)
    return riverslist


def stations_by_river(stations, x = False):
    """Takes a list of MonitoringStation objects and an optional True statement. Returns a dictionary that maps river names to a list of station objects, sorted in alphabetical order if given True."""
    riverstations = {}
    allrivers = rivers_with_station(stations)
    for i in range(len(allrivers)):
        tempstations = []
        for j in range(len(stations)):
            if (stations[j].river) == (allrivers[i]):
                tempstations.append(stations[j].name)
        if x == True:
            tempstations.sort()
        riverstations[allrivers[i]] = tempstations
    return riverstations


def rivers_by_station_number(stations, N):
    #gets river names
    riverName = []
    for i in range(len(stations)):
        current_river = stations[i].river

        exists = False
        for j in range(len(riverName)):
            if riverName[j] == current_river:
                exists = True
                break
        
        if not exists:
            riverName.append(current_river)

#counts no. stations per river
    stationCount = []
    for j in range(len(riverName)):
        numStations = 0
        for e in range(len(stations)):
            if riverName[j] == stations[e].river:
                numStations += 1
        
        stationCount.append((riverName[j], numStations))
    #sorts
    stationCount.sort(key=lambda x: x[1], reverse=True)
    

    #checking for ties
    if len(stationCount)<= N:
        return stationCount[:N]
    

    cutoff = stationCount[N-1][1]

    result = stationCount[:N]

    #adds on any extra tied items after the cutoff value 
    for i in range(N,len(stationCount)):
        if stationCount[i][1] == cutoff:
            result.append(stationCount[i])
        else:
            break
    return result       
