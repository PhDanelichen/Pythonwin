#Import arcpy module
import arcpy
import time
import os.path
#import the environment settings and spatial analyst extension
from arcpy import env
from arcpy.sa import *


#Multiplicando pelo fator de escala = 0.0001 (unidades em Kg C m^-2)


arcpy.env.workspace = r"F:/Artigo_GPP_RPPN/Produto_MOD17A2/2001/MODIS MOD17A2" # from your pathname

#List all images IMGs
rasterList = arcpy.ListRasters("*", "TIF") #Encontro apenas os arquivos que sao tif e com nome "new2"
print "imagens contidas na pasta sao:"
print "---------------------------------------------------------"

for raster in rasterList:
    print raster

      
# Execute Copy
    result_2 = os.path.splitext(raster) [0] + "_2.tif" #"Output_" + raster
    eq = (Float(raster)/10000)
    eq.save(result_2)        
    
    print "--------------------------------------"  
    print result_2
    print "Pronto!"




