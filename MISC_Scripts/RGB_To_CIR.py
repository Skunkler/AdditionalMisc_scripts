import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
DataFrame1 = arcpy.GetParameterAsText(0)
df = arcpy.mapping.ListDataFrames(mxd, DataFrame1)[0]
source_layer =  arcpy.mapping.Layer(r"\\storage\snwa\resrepo\snwagis\common\Imagery_QAQC\CIR_4band.lyr")
for lyr in arcpy.mapping.ListLayers(mxd):
    x = lyr.name
    image = x[-3:]
    if image == "tif":

        arcpy.mapping.UpdateLayer(df, lyr, source_layer, True)
del lyr, mxd
      
