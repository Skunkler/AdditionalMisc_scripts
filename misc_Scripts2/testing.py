import arcpy
from arcpy import env

env.workspace = r"E:\2016_ClarkCounty_imageryclassification\LAS_POINTS_Process\LiDAR_products\Tree_Final_Dataset.gdb"
OutFile = open(r"H:\testing\Tree_fcs.csv", "w")
env.overwriteOutput = True

FCS = arcpy.ListFeatureClasses()

for fc in FCS:
    OutFile.write(fc[5:10] + '\n')
OutFile.close()

