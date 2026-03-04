from floodsystem.geo import *
from floodsystem.stationdata import build_station_list


#defining unit tests:

def test_stations_by_distance():
    st_erth = (50.1654,-5.4309)
    stations = build_station_list()
    y = stations_by_distance(stations, st_erth)
    assert y[0][0].name == "St Erth"
    assert y[0][0].town == "St Erth"
    assert y[0][1] == 0.9581162895158936


def test_stations_within_radius():
    st_erth = (50.1654,-5.4309)
    stations = build_station_list()
    y = stations_within_radius(stations, st_erth, 10)
    x= []
    for i in range(len(y)):
        x.append(y[i].name)
    assert "St Erth" in x
    assert "Relubbus" in x
    assert "Penzance Tesco" in x


def test_rivers_with_station():
    stations = build_station_list()
    y = rivers_with_station(stations)
    assert "Mickley Dyke" in y
    assert "River Cam" in y
    assert "River Hayle" in y
    assert len(y) == 1065


def test_stations_by_river():
    stations = build_station_list()
    y = stations_by_river(stations)
    assert "River Thames" in y
    assert len(y["River Cam"]) == 6
    assert len(y["River Hayle"]) == 2




#running tests:

test_stations_by_distance()
test_stations_within_radius()
test_rivers_with_station()
test_stations_by_river()