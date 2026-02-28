from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Takes list of station objects and returns a list of tuples of stations and their relative water level for stations where the relative water level is over tol, sorted by relative level in descending order"""
    over = []
    for i in range(len(stations)):
        if stations[i].relative_water_level() is not None:
            if stations[i].relative_water_level() > tol:
                over.append((stations[i], stations[i].relative_water_level()))
    return sorted_by_key(over, 1, reverse=True)


def stations_highest_rel_level(stations, N):
    """Takes list of statio objects and returns the N stations with highest relative water levels as a list of tuples"""
    full = []
    for i in range(len(stations)):
        if stations[i].relative_water_level() is not None:
            full.append((stations[i], stations[i].relative_water_level()))
    full = sorted_by_key(full, 1, reverse=True)
    return full[:N]