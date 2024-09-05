import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../map_n_contour')))
from utils import printMinMax

aaaa = np.random.rand(5, 5)  # Random 5x5 array

printMinMax(aaaa, var_name = "aaa")  # Print the minimum and maximum values of the array