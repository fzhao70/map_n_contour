Module map_n_contour.utils
==========================

Functions
---------

`fillnan(arr)`
:   Interpolate missing values (NaN) in a 1D numpy array.
    
    Parameters:
    arr (numpy.ndarray): 1D array with possible NaN values
    
    Returns:
    numpy.ndarray: Array with NaN values filled by linear interpolation

`printMinMax(values, var_name=None)`
:   Print the minimum and maximum values of a numpy array
    
    The reason the name is changed from print_min_max to snake_case printMinMax is to follow the NCL naming convention.

`smooth_savgol(data, window_length=11, polyorder=2)`
:   Smooths the input data using the Savitzky-Golay filter.
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