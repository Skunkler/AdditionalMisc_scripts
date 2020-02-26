#This script was written by Warren Kunkler on 09/12/2016 in support of the water rights hearings project. The result of running this
#script is that it moves all the image files that are outside of the summer time span to a separate out_of_range_folder within each 
#directory as well as create a log file of all the images that were moved 
import os, shutil


#input the directory in which you want to move files
input_path = r"S:\RS_hearings_2017\quicklooks\p40r33"
#output_file = open(input_path + "\\" + "LandSat_out_of_range_log.txt", "w")

for root, dirs, files in os.walk(input_path):
    for filename in files:
        if filename[-16::1] != "Thumbs.db" and len(root) > 49:
            filename_actual = filename[-16::1]
            file_day_str = filename_actual[5:8]
            file_day_num = int(file_day_str)
            if file_day_num >= 90 and file_day_num < 120:
                line = filename_actual[:5] + file_day_str + filename_actual[8:]
                line2 = line+'\n'
                #line3 = root + "\\" + "April_dates"
                    #output_file.write(line2)
                    #Source_path = os.path.join(root, line)
                in_path = os.path.join(root, line)
                line3 = root[:42] + '\\' + line
                


                    #if not os.path.exists(line3):
                    #    try:
                    #        os.makedirs(line3)
                    #    except:
                    #        output_file.write("error with " + line3)
                shutil.move(in_path, line3)
#output_file.close()
            
