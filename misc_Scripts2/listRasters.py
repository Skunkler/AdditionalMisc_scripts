import arcpy
from arcpy import env

env.workspace = r'S:\LV_Valley_Imagery\2018\delivery_20180913'
outFile = open(r'D:\rasterDelivery0913.txt','w')
rasters = arcpy.ListRasters()

for raster in rasters:
    #rasterName = raster[:-4]
    print "'{rasterFile}'".format(rasterFile = raster[:-4])
    outFile.write("'{rasterFile}',".format(rasterFile = raster[:-4]) +'\t' + '\n')
outFile.close()
