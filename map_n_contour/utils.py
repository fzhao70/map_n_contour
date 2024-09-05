import numpy as np

def printMinMax(values, var_name=None):
    """Print the minimum and maximum values of a numpy array
    
    The reason the name is changed from print_min_max to snake_case printMinMax is to follow the NCL naming convention.
    """
    minimum = np.min(values)
    maximum = np.max(values)
    
    if var_name is not None:
        print(f"'{var_name[0]}' : Minimum : {minimum}, Maximum : {maximum}")
    else:
        print(f"Minimum value: {minimum}, Maximum value: {maximum}")
    