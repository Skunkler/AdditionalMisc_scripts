#This script was written by Warren Kunkler on 8/29/2016 in support of the 2016 Clark County Lidar Project. The final product of this
#script is a table of data generated from LASTools that can be joined to the data in mars based on the ID field

import os



#input1_ws points to the directory where all the info files you'd like to compile are
input1_ws = r"L:\Lidar\_ClarkCounty_2016\Vendor_Products\Vendor_Processed_LAS\Preliminary_LAS_tiles\QL2"
#"L035-1-160424A-C1_r_info.txt"


#prompts the user for input as to the QL level of the LiDAR data
QL = raw_input("Please enter QL level for info files: ")



#creates a writeVar that outputs the final product located in the same directory where the rest of info files are but must add on the name extension
writeVar = open(input1_ws + '\\', 'w')

#writes the first line to the compiled file, this acts as the column headers for the final product
writeVar.write("ID\t" + "QL\t" + "last\t" + "Density(All)\t" + \
                           "Density(Last)\t" + "Spacing(All)\t" + "Spacing(Last)\t" + "Min_Elevation\t" + "Max_Elevation\t" + "Unclass\t" + "Ground\t" + "Bridge\t" + "Withheld\n")

#initialize an empty list
Content_List = []


#loop through all the files in the directory and sub directories. if the files are info files begin appending them to the
#Content_List
for root, dirs, files in os.walk(input1_ws):
    for filename in files:
        if filename[-8::1] == "info.txt":

            #Table key is the name of the las file with the extention added on and is used as a key
            #to join with the table for the Mars_QL_Scan collection data
            Table_Key = filename[0:5] + '.las' + '\t'

            #defines the readfile variable as an object that reads the text in each info file, and temporarily appends
            #the lines from that info into the Content_list
            ReadFile_Name = input1_ws + '\\' + filename
            readVar = open(ReadFile_Name, 'r')

            for i in readVar:
                Content_List.append(i)
            readVar.close()

            print len(Content_List)

            Min_Elevation = Content_List[18][-9:-1:1] + '\t'
            

            #defines last returns, point density, and spacing based on their common location within each info file
            Last_Returns = Content_List[47][-15:-1:1] + '\t'
            
            Point_Density1 = Content_List[50][-40:-35:1] + '\t'
            Point_Density2 = Content_List[50][-25:-20:1] + '\t'
            Spacing1 = Content_List[51][-31:-27:1] + '\t'
            Spacing2 = Content_List[51][-16:-12:1] + '\t'
            #warnings = Content_List[52:57]
            Max_Elevation = Content_List[19][-9:-1] +'\t'
            QL_Level = QL + '\t'
            Class1 = Content_List[54][8:16] + '\t'
            Class2 = Content_List[55][8:16] + '\t'

            #writes everything to the output text with the proper formatting to make the file a table 
            writeVar.write(Table_Key)
            writeVar.write(QL_Level)
            writeVar.write(Last_Returns)
            writeVar.write(Point_Density1)
            writeVar.write(Point_Density2)
            writeVar.write(Spacing1)
            writeVar.write(Spacing2)
            writeVar.write(Min_Elevation)
            writeVar.write(Max_Elevation)
            writeVar.write(Class1)
            writeVar.write(Class2)

            if len(Content_List) > 56 and Content_List[56][12:16] != " as ":
                Class3 = Content_List[56][12:16] + '\t'
                Class4 = " \n"
                writeVar.write(Class3)
                writeVar.write(Class4)
            elif len(Content_List) > 56 and Content_List[56][12:16] == " as ":
                Class3 = ' \t'
                Class4 = Content_List[56][27:34] + '\n'
                writeVar.write(Class3)
                writeVar.write(Class4)
                print "Class 4 is " + Class4
            elif len(Content_List) <= 56:
                Class3 = ' \t'
                Class4 = ' \n'
                writeVar.write(Class3)
                writeVar.write(Class4)

            
            
            
            """writeVar.write(Table_Key)
            writeVar.write(QL_Level)
            writeVar.write(Last_Returns)
            writeVar.write(Point_Density1)
            writeVar.write(Point_Density2)
            writeVar.write(Spacing1)
            writeVar.write(Spacing2)
            writeVar.write(Min_Elevation)
            writeVar.write(Max_Elevation)"""

            
            #delete the temporary data in the Content_List variable so that it is an empty list for the next iteration
            del Content_List[:]
            

            
writeVar.close()






