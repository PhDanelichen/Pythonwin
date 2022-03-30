#Import arcpy module
import arcpy
import time
import os.path
#import the environment settings and spatial analyst extension
from arcpy import env
from arcpy.sa import *


arcpy.env.workspace = r"F:/Artigo_GPP_RPPN/Produto_MOD17A2/2001/MODIS MOD17A2" # Coloque o caminho da pasta onde estao as imagens HDFs
#List all images IMGs
rasterList = arcpy.ListRasters("*", "HDF") #find all IMGs images
print "imagens contidas na pasta sao:"
print "---------------------------------------------------------"
for raster in rasterList:
    print raster

    result = os.path.splitext(raster) [0] + "_new.tif" #"Output_" + raster #variavel de saida com nome novo
    eq = arcpy.ExtractSubDataset_management(raster, result, "0") #funcao de recorte by Mask
 
    print result
    print "Pronto!"




