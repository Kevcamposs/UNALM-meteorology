# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 16:10:37 2022

@author: Kevin
"""
import os, numpy as np
from osgeo import gdal

path = r'C:\Users\Kevin\Desktop\UNALM\OctCiclo\Senso_rem'
os.chdir(path)

# Carga de imagen y transformación a array
img = 'Image\\LC08_L1TP_007068_20170424_20170502_01_T1_B2.TIF'
img_open = gdal.Open(img)

################# Clip with mask - GDAL #################
# Carga de Shapefile
shp = r'C:\Users\Kevin\Documents\GIS_files\SHP\QLurín_basin__18N.shp'

# Clip
img_clip = gdal.Warp('Lab_3\\Clip_mask.TIF', # Carpeta destino
                     img_open,               # Array a cortar
                     cutlineDSName = shp,    # Shapefile
                     cropToCutline = True,   # Activar clip
                     dstNodata= np.nan)      # Completar valores

################# Clip with points - GDAL #################
# Carga de points
points = [288651.0196189094567671,    # X mínima
          -1307771.4735176989343017,  # Y mínima
          371836.6587493440601975,    # X máxima
          -1360643.7017785683274269]  # Y máxima

# Clip
img_clip = gdal.Translate('Lab_3\\Clip_points.TIF', # Carpeta destino
                          img_open,                 # Array a cortar
                          projWin = points)         # Shapefile

################# Visualización del recorte #################
import matplotlib.pyplot as plt, geopandas as gpd, rasterio as rio, numpy as np

# Normalización
def Normalize(a): 
    a_2 = np.nanpercentile(a, 2); a_98 = np.nanpercentile(a, 98)
    return (a - a_2)/(a_98 - a_2)

# Cargar ráster (imagen)
clip = rio.open('Lab_3\\Clip_points.TIF')
clip_transform = clip.transform
clip = Normalize(clip.read(1))

# Cargar shapefile - cuenca Lurín
basin = gpd.read_file(r'C:\Users\Kevin\Documents\GIS_files\SHP\Lurin_basin_18N.shp')                      

# Visualización
fig, ax = plt.subplots(1,1, figsize = (8,6))
rio.plot.show(clip, transform = clip_transform, cmap = 'Blues',
              title= 'Cuenca Lurín: Banda 2 (Blues) - Landsat 8', ax = ax)
basin.boundary.plot(ax = ax, color = 'black', markersize=4)
plt.savefig('Lab_3\\img_clip.jpg', dpi = 300)