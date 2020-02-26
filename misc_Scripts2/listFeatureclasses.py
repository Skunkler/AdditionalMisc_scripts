import arcpy, shutil, sys, string, os
from arcpy import env

env.workspace=r'D:\LiDAR_factor\PolysOutput.gdb'

fcs = arcpy.ListFeatureClasses()
#fileOutput = open(r'D:\outPut.csv', 'w')

output = r'D:\LiDAR_factor\2016_LiDAR_study\studyAreaLiDAR.gdb'
FCList = []

for fc in fcs:
    FCList.append(fc[5:11])

env.workspace = r'D:\2016_ClarkCounty_imageryclassification\updateRecords\AccuracyAssessment.gdb'
fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    if fc[5:11] in FCList:
        print fc
        arcpy.FeatureClassToFeatureClass_conversion(fc, output, fc)


#fileOutput.close()
