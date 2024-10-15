Module map_n_contour.draw
=========================

Functions
---------

`figure_format_setting(ax, id)`
:   Setting the format of the figure for the publication
    Useful when you want to have a consistent format for all the figures

`format_basic(ax)`
:   

`format_diurnal(ax, interval=2)`
:   

`format_time_series(ax, interval=<matplotlib.dates.HourLocator object>)`
:   

`map_add_element(ax, province_width=0.3, ifroad=False, ifocean=False)`
:   Add elements to the map

`map_add_gl(ax, labelsize=4)`
:   

`map_ordinary(fig, pos: int)`
:   Setting map on the current axes

`map_setting_lambert(fig, pos: int, lat0: float, lon0: float, lat1: float, lat2: float)`
:   Setting map on the current axes

`style_contourf(ax, lon2d: numpy.ndarray, lat2d: numpy.ndarray, data2d: numpy.ndarray, cmap_name='jet', vint=None, **kwargs)`
:   A simple wrapper for contourf