import numpy as np
from datetime import datetime 

def polyfit(dates, levels, p):
    
    d0 = dates[0]  # time shift - subtract to avoid large numbers 
    t = np.array([(d - d0).days for d in dates], dtype=float)
    
    # Fit a polynomial of degree p to the data
    coeffs = np.polyfit(t, levels, p)
    poly = np.poly1d(coeffs)

    return poly, d0