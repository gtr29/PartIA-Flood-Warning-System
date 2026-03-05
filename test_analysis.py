import numpy as np
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit

def test_polyfit():
    d0 = datetime(2024, 1, 1)
    dates = [d0, d0 + timedelta(days=1)]
    levels = [1.0, 2.0]
    
    poly, start_date = polyfit(dates, levels, 1)
    assert start_date == d0, "Error: start_date is wrong"
    assert round(poly(0)) == 1, "Error: poly(0) should be 1.0"
    assert round(poly(1)) == 2, "Error: poly(1) should be 2.0"
    
    print("passed")

test_polyfit()