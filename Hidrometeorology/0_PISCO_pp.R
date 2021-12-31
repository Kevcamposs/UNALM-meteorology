library(raster)
library(ncdf4)
########## Descript PISCOpm  ############
# Resolución: 0.1° x 0.1° (~10 km)
# Data: 1981 - 2016

########## IMPUT ###########
lon_lat <- read.csv('SanLazaroEscomarca.csv', sep = ';', header = TRUE) # Estaciones
raster_pp_m <- raster::brick('D:\\Data\\PISCO\\PISCOp_v2.1_m.nc') # modelo: pp mensual; 'brick = bloque'

########### PROCESS ##########
sp::coordinates(lon_lat) <- ~Lon+Lat # Establecer coordenadas

# PLot
raster::projection(lon_lat) <- raster::projection(raster_pp_m) 
plot(raster_pp_m[[1]])
plot(lon_lat, ad=T)

# Precipitación mensual

pp_m_values <- raster::extract(raster_pp_m, lon_lat, method = 'simple')
pp <- data.frame(t(pp_m_values))
colnames(pp) <- as.character(lon_lat$Nombre)


########## OUTPUT ##########
write.csv(pp, "pp_m.csv", quote = F, row.names = F)
