#__________________________________________________________________________________________________________
# PROGRAMA PARA TRATAR DO PRODUTO MOD17A GPP DO MODIS: EXTRAÇÃO EM TIF, CORREÇÃO DE FATOR DE ESCALA
# DEFININDO PROJEÇÃO E RECORTE EM LOTE USANDO UMA SHAPE
# DANELICHEN 2015
#__________________________________________________________________________________________________________

#Import arcpy module
import arcpy
import time
import os.path
#import the environment settings and spatial analyst extension
from arcpy import env
from arcpy.sa import *
# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

arcpy.env.workspace = r"E:/Artigo_GPP_RPPN/Produto_MOD17A2/2001/MODIS MOD17A2/" # Coloque o caminho da pasta onde estao as imagens HDFs

#Measuring execution time from program
inicial = time.time()

#____________________________________________________________________________________________________________
#ETAPA 1: EXTRAINDO UMA IMAGEM TIF DE UM CONJUNTO DE IMAGEM HDF PRODUTO GPP MOD17A

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

#____________________________________________________________________________________________________________
#ETAPA 2: Multiplicando pelo fator de escala = 0.0001 (unidades em Kg C m^-2)


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

#____________________________________________________________________________________________________________
# ETAPA 3: MUDANDO A PROJEÇÃO PARA WGS84 21S

#List all images IMGs
if os.path.exists("E:/Artigo_GPP_RPPN/Produto_MOD17A2/2001/MODIS MOD17A2/"): #COLOCA NOVAMENTE O CAMINHO DA PASTA DAS IMAGENS
    rasterList = arcpy.ListRasters("*"+"new_2*", "TIF") #Encontro apenas os arquivos que sao tif e com nome "new2"
    print "imagens contidas na pasta sao:"
    print "---------------------------------------------------------"

    for raster in rasterList:
        print raster

#Redefindo projeção
#verifica se os arquivos existem
        result_3 = os.path.splitext(raster) [0] + "_WGS84.tif" #"Output_" + raster

        arcpy.ProjectRaster_management(raster, result_3, "PROJCS['WGS_1984_UTM_Zone_21S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-57.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NEAREST", "926,625433055833 926,625433055833", "", "", "PROJCS['Unknown_datum_based_upon_the_custom_spheroid_Sinusoidal',GEOGCS['GCS_Unknown_datum_based_upon_the_custom_spheroid',DATUM['D_Not_specified_based_on_custom_spheroid',SPHEROID['Custom_spheroid',6371007.181,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Sinusoidal'],PARAMETER['false_easting',0.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',0.0],UNIT['Meter',1.0]]")

        print "imagem reprojetada!"

#_________________________________________________________________________________________________________
#ETAPA 4: RECORTANDO EM LOTE COM UMA SHAPE 

#List all images IMGs
rasterList = arcpy.ListRasters("*"+"WGS84*", "TIF") #find all IMGs images somente as que tem WGS no nome
print "imagens contidas na pasta sao: "
print "---------------------------------------------------------"

for raster in rasterList:
    print raster

    classe_shape_shp = "E:/Artigo_GPP_RPPN/Shape_RPPN/RPPN_SESC_Pantanal.shp" #pasta onde contem a shape
    result_4 = os.path.splitext(raster) [0] + "_recor.img" #"Output_" + raster #variavel de saida com nome novo
    eq = arcpy.gp.ExtractByMask_sa(raster, classe_shape_shp, result_4) #funcao de recorte by Mask
 
    print result_4
    print "Pronto!"

fim = time.time()
print "Tempo de execucao:"
print ("%.2f" %(fim - inicial), "segundos")
print ("%.2f" %((fim - inicial)/60), "minutos")