# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:29:30 2022

@author: Kevin
"""
import os
from composite_L8 import composite_L8

# Definir carpeta de trabajo
os.chdir(r'C:\\Users\\Kevin\\Desktop\\UNALM\\OctCiclo\\Senso_rem\\Lab_3')

shp = r'C:\Users\Kevin\Documents\GIS_files\SHP\Lurin_basin_18N.shp'

# Carga de imágenes
b2 = r'B2_Lurin.TIF'; b5 = r'B5_Lurin.TIF'; b6 = r'B6_Lurin.TIF'

images = [b6, b5, b2]   # Combinación 6-5-2: zonas agrícolas

Agricultura = composite_L8(images)
Agricultura.composite()
Agricultura.plot(title = 'Cuenca Lurín - Zonas agrícolas (6-5-2)',
                 output = 'C652_Lurín.jpg', shp = shp)
