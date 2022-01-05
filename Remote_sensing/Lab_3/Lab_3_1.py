# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:56:23 2021

@author: Kevin
"""
################# Visualización mediante GDAL #################
import gdal, os, matplotlib.pyplot as plt, numpy as np

os.chdir(r'C:\Users\Kevin\Desktop\UNALM\OctCiclo\Senso_rem')

# Cargar imagen: Banda 2 (Blue)
img = 'Image\\LC08_L1TP_007068_20170424_20170502_01_T1_B2.TIF'
open_gdal = gdal.Open(img)

img_open = open_gdal.GetRasterBand(1) # Cargar banda
img_L8 = img_open.ReadAsArray()       # Pasar a Array

# Normalización
def Normalize(a): 
    a_2 = np.nanpercentile(a, 2); a_98 = np.nanpercentile(a, 98)
    return (a - a_2)/(a_98 - a_2)

img_L8 = Normalize(img_L8)

# Gráfica
plt.figure(figsize = (8,8))
plt.imshow(img_L8, cmap = 'Blues')
plt.title('Banda 2: Blues', fontsize = 16, color = 'darkblue')
plt.savefig('Lab_3\\img_gdal.jpg', dpi = 300)

################# Visualización mediante Rasterio #################
import matplotlib.pyplot as plt, os, glob, rasterio, numpy as np
os.chdir(r'C:\\Users\\Kevin\\Desktop\\UNALM\\OctCiclo\\Senso_rem')
images = glob.glob('Image\\*[2-4].tif') # Carga de imágenes

# Abrir imágenes
R_B2 = rasterio.open(images[0])
R_B3 = rasterio.open(images[1]); R_B4 = rasterio.open(images[2])

# Transformar a arrays
Array_R_B2 = R_B2.read(1); Array_R_B3 = R_B3.read(1); Array_R_B4 = R_B4.read(1)

# Normalización
def Normalize(a): 
    a_2 = np.nanpercentile(a, 2); a_98 = np.nanpercentile(a, 98)
    return (a - a_2)/(a_98 - a_2)

Array_R_B2 = Normalize(Array_R_B2)
Array_R_B3 = Normalize(Array_R_B3)
Array_R_B4 = Normalize(Array_R_B4)

# Visualización
fig, axes = plt.subplots(1,3, figsize = (15,10))
bands = [Array_R_B2, Array_R_B3, Array_R_B4]
color = ['Blues', 'Greens', 'Reds']

from rasterio.plot import show
for i in range(3):
    show(bands[i], transform=R_B2.transform, cmap = color[i],
         title= f'Banda {i+2}: {color[i]} - Landsat 8', ax = axes[i])
plt.savefig('Lab_3\\plot_rasterio.jpg', dpi = 300)

################# Visualización de shapefile #################
import geopandas as gpd, matplotlib.pyplot as plt

# Lectura de archivos
gdf_1 = gpd.read_file(r'C:\Users\Kevin\Documents\GIS_files\SHP\QLurín_basin__18N.shp')
gdf_2 = gpd.read_file(r'C:\Users\Kevin\Documents\GIS_files\SHP\Lurin_basin_18N.shp')

# Se almacena como geodataframe
print(gdf_1)

fig, ax = plt.subplots(1,1, figsize = (6,6))
gdf_1.plot(ax = ax, color = 'green', alpha = 0.25)
gdf_2.plot(ax = ax, color = 'blue', alpha = 0.25)
ax.set_title('Shapefile - Cuenca Lurín', fontsize = 14, color = 'darkblue')
plt.savefig('Lab_3\\shp_plot.jpg', dpi = 300)
