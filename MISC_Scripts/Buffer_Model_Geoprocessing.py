#This Python script was written by Warren Kunkler on 3/28/2016 in support of the project to improve the Aerial Imagery QA workflow. The end product of this script is a feature class made up
#of multiple circular or semi-circular polygons that act as buffers around the pixels in the imagery where there is over a 20% difference or change between each overlapping
#tiles of imagery. I initially tried to work purely within arcpy but trying to import the models into the geodatabase kept causing numerous errors becouse the dimension and size of the
#hilite imagery wasn't being supported in ArcMap for some reason. I found that the os.walk method solved this problem


import arcpy, os, string, time, datetime, shutil, sys, traceback
from arcpy import env

#defines workspace and sets overwrite output to true
ws = r""                               
env.workspace = ws                                                                                  
arcpy.env.overwriteOutput = True


#defines raster_list as a the string pointing to the directory where all the difference polygon rasters are located
raster_list = r""                                                                                                                                                  

#defines variable for temporary computational file
VectorPoly_Layer = "VectorPoly_Layer"                                                               


#destroys any previous version of the template feature class within the workspare geodatabase then proceedes to create a new one from scratch with the proper schema
if arcpy.Exists("Template"):
    arcpy.Delete_management("Template")


spatial_reference = arcpy.Describe("").spatialReference
arcpy.CreateFeatureclass_management(ws, "Template", "POLYGON", "", "DISABLED", "DISABLED", spatial_reference)
arcpy.AddField_management("Template", "gridcode2", "LONG")

logName = raster_list + "\\" + 'Buffer_Geoprocessing.log'
outfile = open(logName, 'w')

outfile.write('\n' + ws  + " ----------------------------------------" '\n')

#expression and codeblock used in the for loop to reorganize the fields in the VectorPoly_Layer feature class so that the proper schema is established with the Template feature class
expression = "getGridcode2(!gridcode!)"

codeblock = """def getGridcode2(ID):
    return ID"""
timeYearMonDay = datetime.date.today()
timeHour = time.localtime()[3]
timeMin = time.localtime()[4]
outfile = open(logName, 'a')
                                                                                             
for root, dirs, files in os.walk(raster_list):                      #used the recursive os.walk method through the directory
    for fileName in files:                                  
        if fileName[-4::1] == ".img":                               #defines vector_Out                                            
            vector_Out = ws + "\\" + "vector_Out1"
            
            try:
                outfile.write("The processing for " + fileName + " is starting")
                outfile.write(fileName + " " + str(timeYearMonDay) + " " + str(timeHour) + ":" + str(timeMin) + '\n')
            
                arcpy.RasterToPolygon_conversion(raster_list + "\\" + fileName, vector_Out)                                     #runs a raster to polygon conversion for each hilight polygon image
                arcpy.MakeFeatureLayer_management(vector_Out, VectorPoly_Layer)                                                 #create a temporary computational file called VectorPoly_Layer
                arcpy.AddField_management(VectorPoly_Layer, "gridcode2", "LONG")                                                #establishes new field in VectorPoly_Layer
                arcpy.CalculateField_management(VectorPoly_Layer, "gridcode2", expression, "Python_9.3", codeblock)             #calculates that field based on original gridcode
                arcpy.DeleteField_management(VectorPoly_Layer, ["Id", "gridcode"])                                              #deletes Id and gridcode columns so that the schema between the VectorPoly_Layer and Template feature class will lock
                arcpy.SelectLayerByAttribute_management(VectorPoly_Layer, "NEW_SELECTION", "gridcode2 = 1")                     #selects where there are buffer polygons within each VectorPoly_Layer
                arcpy.Append_management(VectorPoly_Layer, "Template")                                                           #append the buffer polygons within VectorPoly_Layer to Template
                arcpy.Delete_management(VectorPoly_Layer)                                                                       #delete VectorPoly_Layer and vector_Out will be overwritten with each iteration of the for loop
            except:
                outfile.write("Process failed for " + fileName)
                                                                                                                            
  
arcpy.Dissolve_management("Template", "Final_fc_Output", "", "", "SINGLE_PART")                                                                    #Dissolve all overlaping polygons in Template                                         #split the multipart polygon that is Final_fc_Output to a final product called Template_SinglePart2

outfile = open(logName ,'a')    
outfile.write("Process Complete "  + str(timeYearMonDay) +  " " + str(timeHour)+ ":" + str(timeMin) +  '\n' ) 
outfile.close()

print("Process done! " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin))

