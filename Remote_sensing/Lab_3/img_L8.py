# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:05:16 2022

@author: Kevin
"""
class img_L8:
    def __init__(self, img, normalize = True):
        self.img = img
        import rasterio as rio, numpy as np
        
        self.img_ar = rio.open(self.img).read(1)
        self.crs = rio.open(self.img).transform
        
        if normalize == True:
            a_2 = np.nanpercentile(self.img_ar, 2)
            a_98 = np.nanpercentile(self.img_ar, 98)
            self.img_ar = (self.img_ar - a_2)/(a_98 - a_2)
        
        return print('La imagen se cargó correctamente.')
    
    def plot(self, title = 'Landsat 8', transform = True, cmap = 'gray'):
        from rasterio.plot import show
        if transform == True:
            show(self.img_ar, transform = self.crs, title = title, cmap = cmap)
        else:
            show(self.img_ar, title = title, cmap = cmap)
    
    def clip_shp(self, shp, output):
        from osgeo import gdal
        import numpy as np
        gdal.Warp(output, self.img, cutlineDSName = shp,cropToCutline = True, dstNodata= np.nan)
        return print('Proceso finalizado.')
        
    def clip_points(self, points, output):
        from osgeo import gdal
        gdal.Translate(output, self.img, projWin = points)
        return print('Proceso finalizado.')