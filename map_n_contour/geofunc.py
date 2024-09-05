import numpy as np

def distance_ll(lon1, lat1, lon2, lat2):
    """Calculate the distance between two points on the Earth's surface
    """
    # Convert degrees to radians
    lon1_rad = np.radians(lon1)
    lat1_rad = np.radians(lat1)
    lon2_rad = np.radians(lon2)
    lat2_rad = np.radians(lat2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = np.sin(dlat/2)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return 6371 * c  # Radius of the Earth in kilometers

def calculate_grid_cell_area(lon2d, lat2d):
    """Calculate the area of each grid cell in a 2D grid of latitudes and longitudes
    """
    from pyproj import Geod

    geod = Geod(ellps="WGS84")
    nrows, ncols = lon2d.shape
    area = np.zeros((nrows, ncols))  # Initialize the area array with the same size as lon2d and lat2d
    for i in range(nrows-1):
        for j in range(ncols-1):
            # Get the corners of the grid cell
            lon_ul, lat_ul = lon2d[i, j], lat2d[i, j]  # upper left
            lon_ur, lat_ur = lon2d[i, j+1], lat2d[i, j+1]  # upper right
            lon_ll, lat_ll = lon2d[i+1, j], lat2d[i+1, j]  # lower left
            lon_lr, lat_lr = lon2d[i+1, j+1], lat2d[i+1, j+1]  # lower right

            # Calculate the area of the quadrilateral
            lons = [lon_ul, lon_ur, lon_lr, lon_ll, lon_ul]
            lats = [lat_ul, lat_ur, lat_lr, lat_ll, lat_ul]
            cell_area, _ = geod.polygon_area_perimeter(lons, lats)
            
            # Convert the area to square kilometers
            cell_area_km2 = np.abs(cell_area) / 1e6
            
            # Assign the calculated area to the appropriate grid cells
            area[i, j] += cell_area_km2 / 4
            area[i, j+1] += cell_area_km2 / 4
            area[i+1, j] += cell_area_km2 / 4
            area[i+1, j+1] += cell_area_km2 / 4

    return area