import arcpy
from arcpy import env

env.workspace = r"H:\missing_sets\workSpace.gdb"

env.overwriteOutput = True

fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    spatial_ref = arcpy.Describe(fc).spatialReference
    if '{0}'.format(spatial_ref.name) == "North_American_1983_Transverse_Mercator" and fc[-4:] == "_veg": 
        print "correcting features with " + fc
        with arcpy.da.UpdateCursor(fc, ['SHAPE@XY']) as cursor:
            for row in cursor:
                cursor.updateRow([[row[0][0] + (-3.2979), row[0][1] + (1.78)]])
        
