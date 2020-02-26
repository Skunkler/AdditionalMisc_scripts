# This script recursively loops code through workspaces looking for ArcGIS datasets and feature classes
# for processing.  You have to set a base workspace to start the recursive "search".  A log file for the
# geoprocessing is written to the base workspace.

import arcpy, os, sys, string, time, datetime, shutil, traceback
from arcpy import env
arcpy.SetLogHistory(True)
#set the workspace path
BaseWS = raw_input(" Enter the workspace path: ")
env.workspace = BaseWS
logpath = BaseWS

#set the log file name to the script name
scriptName = sys.argv[0]
logName = sys.argv[0].split("\\")[len(sys.argv[0].split("\\")) - 1][0:-3]
logfile = logpath + "\\" + logName + ".log"

#set the overwriteoutput to true or false
arcpy.env.overwriteOutput = True

       
# create a tuple of local time data        
timeYearMonDay = datetime.date.today()
timeHour = time.localtime()[3]
timeMin = time.localtime()[4]

outfile = open(logfile,'a')
outfile.write(scriptName + " ----- " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) +  '\n')
outfile.close()

         
#walk through folders to enter ArcGIS workspaces and process items within all workspaces below the BaseWS 
folders = []

for root, dirs, files in os.walk(BaseWS):

    folders.append(root)

for WSDir in folders:
    #set the folders below the BaseWS as workspaces to enable the ArcGIS List method on those workspaces
    env.workspace  = WSDir


#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------  
    
#List workspaces
    wslist = arcpy.ListWorkspaces("*", "")
    

#Loop through those workspaces    
    for  gpws in wslist:
        print "workspace = " + gpws
        env.workspace = gpws
        
        #Open the logfile and log workspaces looped through
        outfile = open(logfile,'a')
        outfile.write('\n' + gpws  + '\n')
        

#-------------------------------------------------------------------------------------------------------------------------------
#       GEOPROCESSING GOES BELOW THIS LINE
#-------------------------------------------------------------------------------------------------------------------------------

#List Datasets and feature classes within the workspaces and loop through - this can be modified to process only features or only rasters
 
        DatList = arcpy.ListDatasets("*", "All") #change "all" to "Rasters" if you want to process only rasters
        for  DatSet in DatList:
 
            try:
                #For Rasters - geoprocessing code would go here *************************
                print "dataset = " +  DatSet
                outfile.write("processing " + DatSet+ '\n')
                
            except:
                print "process failed for " + gpws + " " + DatSet
                print arcpy.GetMessages(2)
                ouch = arcpy.GetMessages(2)
                outfile.write(ouch + " process failed for " + gpws + " " + DatSet+ '\n')
                
                 
        fcs = arcpy.ListFeatureClasses("*", "")#change the "" to a specific feature class type if you want to process specific feature class types
        for fc in fcs:
 
            try:
                #For GDB Features - geoprocessing code would go here **************************  
                print "feature class = " + fc
                outfile.write("processing " + fc+ '\n')
                
            except:
                print "process failed for " + gpws + " " + fc
                print arcpy.GetMessages(2)
                ouch = arcpy.GetMessages(2)
                outfile.write(ouch + " process failed for " + gpws + " " + fc+ '\n')
        outfile.close()


#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
 

# create a tuple of local time data
timeYearMonDay = datetime.date.today()
timeHour = time.localtime()[3]
timeMin = time.localtime()[4]

outfile = open(logfile,'a')
outfile.write("Process done! " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin))
outfile.close()

print "Process done! " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) + "*********************************************************************"


