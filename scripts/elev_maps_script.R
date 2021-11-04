setwd("D:/Species_distrib_example")

library(raster)
library(dismo)
library(maptools)
library("RColorBrewer")
library(tmap)
library(tmaptools)
library(maps)
library(spData)


#create elevation map in lat/long and crop to desired coordinates
NAmer_elev <- raster("elevation.tif")
NAmer_elev_geog <- projectRaster(NAmer_elev, crs = '+proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0')
NAmer_elev_geog <- crop(NAmer_elev_geog, c(-117, -94, 18, 37))

#upload point and type data and convert to SpatialPointsDataFrame
Pogo <- read.csv("Pogo.csv", header=T)
coordinates(Pogo) = cbind(Pogo$long, Pogo$lat)
Pogo$Map_type = as.factor(Pogo$Taxon)

#plotting points onto an elevation map with country borders, unknowns identified, Fig. 1
world_shape <- data(world)
palette(c("purple", "orange", "blue", "red", "#006600", "black", "brown"))
types <- palette()
tm_shape(NAmer_elev_geog)+
  tm_layout(legend.outside = TRUE) +
  tm_raster(style="cont", palette=get_brewer_pal("Greys", plot=FALSE)) + 
  tm_shape(world) + tm_borders(col = "black") + 
  tm_shape(Pogo) + tm_bubbles(size = 0.2, palette = types, col = "Taxon", border.col = "black")
#map with FGH collapsed, no unknowns, Fig. 7  
palette(c("orange", "red", "#006600", "black"))
types <- palette()
tm_shape(NAmer_elev_geog)+
  tm_layout(legend.outside = TRUE) +
  tm_raster(style="cont", palette=get_brewer_pal("Greys", plot=FALSE)) + 
  tm_shape(world) + tm_borders(col = "black") + 
  tm_shape(Pogo) + tm_bubbles(size = 0.2, palette = types, col = "ID", border.col = "black")

