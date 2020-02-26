#This script was written by Warren Kunkler on 09/12/2016 in support of the water rights hearings project. The result of running this
#script is that it moves all the image files that are outside of the summer time span as well as creates a log file of all the images
#that were moved 
import os, shutil


#input the directory in which you want to move files
input_path = r"S:\RS_hearings_2017\quicklooks\p40r33"
output_file = open(input_path + "\\" + "LandSat_out_of_range_log.txt", "w")

for root, dirs, files in os.walk(input_path):
    for filename in files:
     
        #looks for only jpgs in all directories that are not cloudy
        if filename[-16::1] != "Thumbs.db" and len(root) != 49:
            #isolates just the file name from the entire source
            filename_actual = filename[-16::1]
            #pulls the day of the year which is in string format
            file_day_str = filename_actual[5:8]

            #makes sure the string number is an actual number and converts it to int
            if file_day_str != "nge":
                file_day_num = int(file_day_str)

                #pull only the numbers below 120 and above 275
                if file_day_num < 120 or file_day_num > 275:

                    #recreates the file name around the actual number we want to pull
                    line = filename_actual[:5] + file_day_str + filename_actual[8:]

                    #this is for the logfile
                    line2 = line+'\n'

                    #this is for the output location to where we are going to move the file
                    line3 = root + "\\" + "out_of_range"
                    output_file.write(line2)
                    #points to the file we want to move
                    Source_path = os.path.join(root, line)

                    #checks to see if the directory where we want to move the file exists, and if not then create it
                    if not os.path.exists(line3):
                        try:
                            os.makedirs(line3)
                        except:
                            output_file.write("error with " + line3)

                    #actually moves the file we want to move to the desired output location
                    shutil.move(Source_path, line3)
output_file.close()
            
