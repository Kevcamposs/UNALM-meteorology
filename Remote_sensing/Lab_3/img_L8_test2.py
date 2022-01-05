# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:07:39 2022

@author: Kevin
"""
######### Clip by mask #############
import os, glob
from img_L8 import img_L8

# Definir carpeta de trabajo
os.chdir(r'C:\\Users\\Kevin\\Desktop\\UNALM\\OctCiclo\\Senso_rem')

# Imagen y creación de objeto
images = glob.glob('Image\\*[2-4].tif') # Carga de imágenes

Banda_2 = img_L8(images[0], normalize = False)
Banda_3 = img_L8(images[1], normalize = False)
Banda_4 = img_L8(images[2], normalize = False)

# Clip con máscara
shp = r'C:\Users\Kevin\Documents\GIS_files\SHP\QLurín_basin__18N.shp'

Banda_2.clip_shp(shp, 'Lab_3\\B2_Lurín.TIF')
Banda_3.clip_shp(shp, 'Lab_3\\B3_Lurín.TIF')
Banda_4.clip_shp(shp, 'Lab_3\\B4_Lurín.TIF')
