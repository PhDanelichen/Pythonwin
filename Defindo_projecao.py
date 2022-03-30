#Import arcpy module
import arcpy
import time
import os.path
#import the environment settings and spatial analyst extension
from arcpy import env
from arcpy.sa import *


#Multiplicando pelo fator de escala = 0.0001 (unidades em Kg C m^-2)


arcpy.env.workspace = r"F:/Artigo_GPP_RPPN/Produto_MOD17A2/2010/MODIS MOD17A2" # from your pathname

#List all images IMGs
if os.path.exists("F:/Artigo_GPP_RPPN/Produto_MOD17A2/2010/MODIS MOD17A2/"):
    rasterList = arcpy.ListRasters("*"+"*new_2*", "TIF") #Encontro apenas os arquivos que sao tif e com nome "new2"
    print "imagens contidas na pasta sao:"
    print "---------------------------------------------------------"

    for raster in rasterList:
        print raster

#Redefindo projeção
#verifica se os arquivos existem
        result_3 = os.path.splitext(raster) [0] + "_WGS84.tif" #"Output_" + raster

        arcpy.ProjectRaster_management(raster, result_3, "PROJCS['WGS_1984_UTM_Zone_21S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-57.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NEAREST", "926,625433055833 926,625433055833", "", "", "PROJCS['Unknown_datum_based_upon_the_custom_spheroid_Sinusoidal',GEOGCS['GCS_Unknown_datum_based_upon_the_custom_spheroid',DATUM['D_Not_specified_based_on_custom_spheroid',SPHEROID['Custom_spheroid',6371007.181,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Sinusoidal'],PARAMETER['false_easting',0.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',0.0],UNIT['Meter',1.0]]")

        print "imagem reprojetada!"
      




