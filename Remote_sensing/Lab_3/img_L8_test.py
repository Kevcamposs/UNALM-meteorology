# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:07:39 2022

@author: Kevin
"""
import os
from img_L8 import img_L8

# Definir carpeta de trabajo
os.chdir(r'C:\\Users\\Kevin\\Desktop\\UNALM\\OctCiclo\\Senso_rem')

# Imagen y creación de objeto
image = r'Image\LC08_L1TP_007068_20170424_20170502_01_T1_B2.TIF'
Banda_2 = img_L8(image)

# Clip con máscara
shp = r'C:\Users\Kevin\Documents\GIS_files\SHP\QLurín_basin__18N.shp'
Banda_2.clip_shp(shp, 'test.TIF')

# Clip con puntos
points = [288651.0196189094567671,    # X mínima
          -1307771.4735176989343017,  # Y mínima
          371836.6587493440601975,    # X máxima
          -1360643.7017785683274269]  # Y máxima

Banda_2.clip_points(points, 'test2.TIF')

# Plot básico
Banda_2.plot(title = 'Landsat 8 - Banda 2 (Blue)',
             cmap = 'Blues')