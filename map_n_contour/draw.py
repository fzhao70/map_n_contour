import copy
import sys
import os
from random import randint
from glob import glob

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import netCDF4 as nc
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.img_tiles as cimgt
import matplotlib as mpl
import matplotlib.dates as md
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size


def map_setting_lambert(fig,
                        pos:int,
                        lat0:float,
                        lon0:float,
                        lat1:float,
                        lat2:float):
    """ Setting map on the current axes
    """
    plt.style.use("seaborn-v0_8-talk")

    lcc = ccrs.LambertConformal(central_latitude=lat0, central_longitude=lon0, standard_parallels=(lat1,lat2))
    ax = fig.add_subplot(pos, projection=lcc)
    states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='10m',
        facecolor='none')

    ax.add_feature(states_provinces, edgecolor='grey', linewidth=0.2)
    ax.add_feature(cfeature.COASTLINE, edgecolor='black')
    ax.add_feature(cfeature.BORDERS, edgecolor='black')
    roads = cfeature.NaturalEarthFeature('cultural','Roads','10m',facecolor='none')
    ocean_mask = cfeature.OCEAN.with_scale('50m')
    ax.coastlines()
    ax.set_aspect('auto')

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
              linewidth=0.6, color='gray', alpha=0.5, linestyle='--',
              x_inline = False, y_inline = False)

    gl.bottom_labels = False
    gl.right_labels = False
    gl.rotate_labels = False
    gl.xlabel_style = {'size': 4, 'color': 'gray'}
    gl.ylabel_style = {'size': 4, 'color': 'gray'}

    return ax, gl

def style_contourf(ax,
                   lon2d:np.ndarray,
                   lat2d:np.ndarray,
                   data2d:np.ndarray,
                   cmap_name ='jet',
                   vint = None,
                   **kwargs):
    """ A simple wrapper for contourf
    """

    # turbo, jet
    cmap = copy.copy(mpl.colormaps[f"{cmap_name}"])
    cmap.set_under(color='white')

    if vint is None:
        vint = np.linspace(np.min(data2d), np.max(data2d), 25)

    bounds = colors.BoundaryNorm(boundaries=vint,ncolors=256)

    cs = ax.contourf(lon2d, lat2d, data2d, 
                     levels=vint, norm= bounds, 
                     transform=ccrs.PlateCarree(), cmap=cmap,
                     extend='both', alpha=0.8, zorder=1)

    return cs

def figure_format_setting(ax, id):
    """ Setting the format of the figure for the publication
    Useful when you want to have a consistent format for all the figures
    """
    plt.style.use("seaborn-v0_8-talk")
    ax.tick_params(labelsize = 'x-large')
    ax.ticklabel_format(axis='y', style='sci')
    ax.yaxis.offsetText.set_fontsize('x-large')
    ax.legend(fontsize = 'x-large')
    ax.grid(True)

    ax.text(0.05, 1.10, f'{id}', transform=ax.transAxes, fontsize = 'xx-large', 
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
    return ax

def format_bar(ax):
    ax.tick_params(labelsize = 'xx-large')
    ax.yaxis.offsetText.set_fontsize('xx-large')
    ax.legend(fontsize = 'xx-large', loc = 'lower right')
    ax.grid(True)
    
    return ax

def format_diurnal(ax, interval = 2):
    ax.tick_params(labelsize = 'xx-large')
    ax.yaxis.offsetText.set_fontsize('xx-large')
    ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
    ax.xaxis.set_major_locator(md.HourLocator(interval = interval))
    ax.xaxis.set_tick_params(rotation=45)
    ax.legend(fontsize = 'xx-large')
    ax.grid(True)
    
    return ax

def format_time_series(ax, interval = md.HourLocator(interval = 2)):
    ax.tick_params(labelsize = 'xx-large')
    ax.yaxis.offsetText.set_fontsize('xx-large')
    ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d %H:%M'))
    ax.xaxis.set_major_locator(interval)
    ax.xaxis.set_tick_params(rotation=45)
    ax.legend(fontsize = 'xx-large')
    ax.grid(True)
    
    return ax