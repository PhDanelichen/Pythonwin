#Import arcpy module
import arcpy
import time
import os.path
#import the environment settings and spatial analyst extension
from arcpy import env
from arcpy.sa import *

#Fazendo médias de todas imagens da pasta (unidades em Kg C m^-2)

arcpy.env.workspace = r"D:/Artigo_GPP_RPPN/WUE_GPP_ET/WUE/2014/chuvosa" # Coloca o caminho da pasta das imagens

arcpy.CheckOutExtension('Spatial')  

#List all images IMGs
rasters = arcpy.ListRasters("*", "IMG") #Encontro apenas os arquivos que sao imagem
print "As imagens contidas na pasta sao:"
print rasters

# Run cell statistics
calc = arcpy.sa.CellStatistics(rasters, statistics_type = "MEAN")
calc.save(r'D:/Artigo_GPP_RPPN/WUE_GPP_ET/WUE/2014/chuvosa/chuvosa_2014.img') #Coloca o caminho da pasta das imagens, colocando o nome da nova imagem "media.img"

print "------------------------------------------------------------------------------"
print "MEDIA FEITA"
print calc
      