# This script loops through feature classes in a single workspace
# Import system modules
import sys, string, os, arcpy, time, datetime, shutil, traceback
from arcpy import env
arcpy.SetLogHistory(True)

#set the workspace path - this calls for user input at runtime and set environment to that workspace
ws = raw_input(" Enter the workspace path: ")
env.workspace = ws

# set the logfile path
##tempsp = raw_input(" Enter the temp space path: ")
logpath = raw_input(" Enter the log file path: ")
#logpath = r"V:\users\brandtj\python_script\logfile_temp"

#error checking on the ws path
if os.path.exists(ws)== False:
    print "Directory: " + root + " does not exist... Bailing out!"
    time.sleep(5)
    sys.exit()

#set overwrite yes or no
arcpy.env.overwriteOutput = True

# set the logfile name to be the name of the script
scriptName = sys.argv[0]
logName = sys.argv[0].split("\\")[len(sys.argv[0].split("\\")) - 1][0:-3]
logfile = logpath + "\\" + logName + ".log"

#------Opens the logfile ********************************************************
outfile = open(logfile,'a')

#------writes script name and ws to logfile ********************************************************
outfile.write('\n' + ws  + '\n' + scriptName + " ----------------------------------------" '\n')
outfile.close()
##



#Loop through the list of feature classes
fcs = arcpy.ListFeatureClasses("", "")

for fc in fcs:

    # create a tuple of local time data
    timeYearMonDay = datetime.date.today()
    timeHour = time.localtime()[3]
    timeMin = time.localtime()[4]
    
    
    #Record the fc and the time processing starts in the log file
    outfile = open(logfile,'a')  
    outfile.write(fc + " " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) +  '\n')


    
#----------------------------------------------------------------------------------------------------------------------------
        #GEOPROCESSING CODE GOES BELOW HERE
#----------------------------------------------------------------------------------------------------------------------------    
    try:
        print fc


    except:
        print "Process: Failed for: " + fc
        print arcpy.GetMessages(2)
        ouch = arcpy.GetMessages(2)
        outfile.write(ouch + '\n' )        
        outfile.write("Process: Failed for: " + fc + " " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) +  '\n' )


      

#----------------------------------------------------------------------------------------------------------------------------    
#----------------------------------------------------------------------------------------------------------------------------    


    outfile.close()

    
# create a tuple of local time data
timeYearMonDay = datetime.date.today()
timeHour = time.localtime()[3]
timeMin = time.localtime()[4]


print "Process done! " + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin)
outfile= open(logfile,'a')
outfile.write("Process Complete "  + str(timeYearMonDay) +  " " + str(timeHour)+ ":"   + str(timeMin) +  '\n' )
outfile.close() 
