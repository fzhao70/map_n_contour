# map_n_contour
A handy map to plot contour on map using python

## To use this library

```
pip install git+https://github.com/fzhao70/map_n_contour.git
```

To uninstall it

```
pip uninstall map_n_contour
```

### API list and Document

[https://fzhao70.github.io/map_n_contour/](https://fzhao70.github.io/map_n_contour/)

## Example to use that

```
from map_n_contour import map_setting_lambert, style_contourf

fig = plt.figure(1, figsize = (10, 10), dpi=200)

ax, gl = map_setting_lambert(fig, 221, lat0, lon0, lat1, lat2)
cs = style_contourf(ax, lon, lat, data1, vint = np.linspace(-2, 2, 20), cmap_name = 'bwr')
ax, gl = map_setting_lambert(fig, 222, lat0, lon0, lat1, lat2)
cs = style_contourf(ax, lon, lat, data2, vint = np.linspace(-2, 2, 20), cmap_name = 'bwr')
ax, gl = map_setting_lambert(fig, 223, lat0, lon0, lat1, lat2)
cs = style_contourf(ax, lon, lat, data3, vint = np.linspace(-2, 2, 20), cmap_name = 'bwr')
ax, gl = map_setting_lambert(fig, 224, lat0, lon0, lat1, lat2)
cs = style_contourf(ax, lon, lat, data4, vint = np.linspace(-2, 2, 20), cmap_name = 'bwr')

```

Simple as that



