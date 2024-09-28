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

def smooth_savgol(data, window_length=11, polyorder=2):
    """
    Smooths the input data using the Savitzky-Golay filter.
    From ChatGPT

    Parameters:
    - data: numpy array
        The input data array to be smoothed.
    - window_length: int, optional (default=11)
        The length of the filter window (i.e., the number of coefficients). 
        `window_length` must be a positive odd integer.
    - polyorder: int, optional (default=2)
        The order of the polynomial used to fit the samples. 
        `polyorder` must be less than `window_length`.

    Returns:
    - smoothed_data: numpy array
        The smoothed data array.
    """
    from scipy.signal import savgol_filter
    
    # Validate window_length
    if window_length % 2 == 0 or window_length < 1:
        raise ValueError("window_length must be a positive odd integer.")
    # Validate polyorder
    if polyorder >= window_length:
        raise ValueError("polyorder must be less than window_length.")
    
    # Apply Savitzky-Golay filter
    smoothed_data = savgol_filter(data, window_length, polyorder)
    return smoothed_data