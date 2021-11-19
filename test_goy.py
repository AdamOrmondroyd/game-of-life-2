"""
Test goy.py
"""
import numpy as np
from goy import step, run, BEACON_1, BEACON_2, GLIDER

def oscillator_test():
    """Test whether step does a beacon oscillator correctly"""
    middle = step(BEACON_1)
    end = step(middle)
    assert(np.array_equal(BEACON_2, middle) and np.array_equal(BEACON_1, end))
    
def glider_test():
    """Test whether running a glider 24 steps on a 6x6 gets back to where it started"""
    end_cells = run(GLIDER, 24)
    assert(np.array_equal(GLIDER, end_cells))