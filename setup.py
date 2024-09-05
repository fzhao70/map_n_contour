from setuptools import setup, find_packages

setup(
    name='map_n_contour',  # Name of the library
    version='0.1.0',  # Version
    packages=find_packages(),  # Automatically find all packages in the library
    install_requires=[
        'numpy',  # Dependencies your library needs
        'matplotlib',
        'cartopy',
        'netCDF4',
        'cftime',
        'xarray',
    ],
    author='Fanghe Zhao',
    author_email='fzhao97@gmail.com',
    description='A simple Python library to plot filled contour and more on the map',
    url='https://https://github.com/fzhao70/map_n_contour',  # Project homepage
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)