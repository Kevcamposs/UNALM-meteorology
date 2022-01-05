# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:22:26 2022

@author: Kevin
"""
class composite_L8:
    def __init__(self, img, normalize = True):
        self.img = img
        import rasterio as rio, numpy as np
        
        self.img_ar1 = rio.open(self.img[0]).read(1)
        self.img_ar2 = rio.open(self.img[1]).read(1)
        self.img_ar3 = rio.open(self.img[2]).read(1)
        
        self.crs = rio.open(self.img[0]).transform
        
        if normalize == True:
            def Normalize(a): 
                a_2 = np.nanpercentile(a, 2); a_98 = np.nanpercentile(a, 98)
                return (a - a_2)/(a_98 - a_2)
            
            self.img_ar1 = Normalize(self.img_ar1)
            self.img_ar2 = Normalize(self.img_ar2)
            self.img_ar3 = Normalize(self.img_ar3)

        return print('Las imágenes se cargaron correctamente.')
        
    def composite(self):
        import numpy as np
        self.com = np.stack((self.img_ar1, self.img_ar2, self.img_ar3))
        
        return print('Composite completado.')
    
    def plot(self, title = 'Landsat 8 - composite', save = True, 
             output = 'com.TIF', shp = None):
        import matplotlib.pyplot as plt, rasterio as rio, geopandas as gpd
        
        fig, ax = plt.subplots(1,1, figsize = (10,10))
        
        rio.plot.show(self.com, transform = self.crs, title= title, ax = ax)
        if shp != None:
            shape = gpd.read_file(shp)  
            shape.boundary.plot(ax = ax, color = 'black', markersize=4.5)
        if save == True:
            plt.savefig(output, dpi = 300)
        
        