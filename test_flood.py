from floodsystem.flood import *
from floodsystem.station import MonitoringStation

s_id1 = "test 1"
m_id1 = "test 1"
label1 = "first station"
coord1 = (-2.0, 4.0)
trange1 = (0.0, 10.0)
river1 = "River 1"
town1 = "My Town 1"
s = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
s.latest_level = 9.0


s_id2 = "test 2"
m_id2 = "test 2"
label2 = "second station"
coord2 = (6.0, -1.0)
trange2 = (-2.0, 6.0)
river2 = "River 2"
town2 = "My Town 2"
typical_range1 = (0.0, 10.0)
s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
s2.latest_level = -1.0

def test_stations_level_over_threshold():
    y = stations_level_over_threshold([s,s2], 0.4)
    assert y[0][0].name == "first station"
    assert y[0][1] == 0.9
    assert len(y) == 1


def test_stations_highest_rel_level():
    y  = stations_highest_rel_level([s,s2],2)
    assert y[0][0].name == "first station"
    assert y[0][1] == 0.9
    assert y[1][0].name == "second station"
    assert y[1][1] == 0.125


#run unit tests:
test_stations_level_over_threshold()
test_stations_highest_rel_level()