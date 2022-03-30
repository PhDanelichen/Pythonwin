#Import arcpy module
import arcpy
import time
import os.path
#import the environment settings and spatial analyst extension
from arcpy import env
from arcpy.sa import *
# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

env.workspace = r"F:/Artigo_GPP_RPPN/Produto_MOD17A2/2003/MODIS MOD17A2" # from your pathname

#List all images IMGs
rasterList = arcpy.ListRasters("*"+"WGS84*", "TIF") #find all IMGs images somente as que tem WGS no nome
print "imagens contidas na pasta sao: "
print "---------------------------------------------------------"

for raster in rasterList:
    print raster

    classe_shape_shp = "F:/Artigo_GPP_RPPN/Shape_RPPN/RPPN_SESC_Pantanal.shp" #pasta onde contem a shape
    result_4 = os.path.splitext(raster) [0] + "_recor.img" #"Output_" + raster #variavel de saida com nome novo
    eq = arcpy.gp.ExtractByMask_sa(raster, classe_shape_shp, result_4) #funcao de recorte by Mask
 
    print result_4
    print "Pronto!"
   
    

    

