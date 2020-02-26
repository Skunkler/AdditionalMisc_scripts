#This script was written by Warren Kunkler on 09/12/2016 in support of the water rights hearings project. The result of running this
#script is that it moves all the image files that are outside of the summer time span as well as creates a log file of all the images
#that were moved 
import os, shutil


#input the directory in which you want to move files
input_path = r"S:\RS_hearings_2017\quicklooks\p40r33"
output_file = open(input_path + "\\" + "LandSat_cloudy_log4.txt", "w")

for root, dirs, files in os.walk(input_path):
    for filename in files:
     
        #looks for only jpgs in all directories that are not cloudy
        if filename[-16::1] != "Thumbs.db" and len(root) == 49:
            
            filename_actual = filename[-16::1]
            
            file_day_str = filename_actual[5:8]


                    #recreates the file name around the actual number we want to pull
            line = filename_actual[:5] + file_day_str + filename_actual[8:]
            output_file.write("p40r33" + '\t' + line + '\n')
                    
output_file.close()
            
