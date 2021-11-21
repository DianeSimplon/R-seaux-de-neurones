import numpy as np
from math import *
import pandas as pd

import solutionExercice1 as sl
import pytest as pt

"""X = [1,-3.1,-7.2, 2.1]
W = [2.1, 1.2, 0.3, 1.3]
b = -3"""

@pt.fixture
def test_model(X, W, b):
    som = 0
    for i in range(len(X)):
        som = som + X[i]*W[i]
    Z1 = som + b
    assert sl.model([1,-3.1,-7.2, 2.1], [2.1, 1.2, 0.3, 1.3], -3)
