#This script was written by Warren Kunkler on 8/29/2016 in support of the 2016 Clark County Lidar Project. The final product of this
#script is a table of data generated from LASTools that can be joined to the data in mars based on the ID field

import os



#input1_ws points to the directory where all the info files you'd like to compile are
input1_ws = r"L:\Lidar\_ClarkCounty_2016\Vendor_Products\Vendor_Processed_LAS\Final_LAS_v1_4\QL2"
#"L035-1-160424A-C1_r_info.txt"


#prompts the user for input as to the QL level of the LiDAR data
QL = raw_input("Please enter QL level for info files: ")



#creates a writeVar that outputs the final product located in the same directory where the rest of info files are but must add on the name extension
writeVar = open(input1_ws + '\\compiled_lasinfo.txt', 'w')

#writes the first line to the compiled file, this acts as the column headers for the final product
writeVar.write("ID\t" + "QL\t" + "last\t" + "Density(All)\t" + \
                           "Density(Last)\t" + "Spacing(All)\t" + "Spacing(Last)\t" + "Min_Elevation\t" + "Max_Elevation\t" + "Unclass\t" + "Ground\t" + "Noise\t" + "Water\t" + "Ignored\t" + "Bridge\t" + "H_Noise\t" + "Withheld\n")

#initialize an empty list
Content_List = []


#loop through all the files in the directory and sub directories. if the files are info files begin appending them to the
#Content_List
for root, dirs, files in os.walk(input1_ws):
    for filename in files:
        if filename[-8::1] == "info.txt" and filename != "10326_info.txt" and filename != "19213_info.txt":

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

            Info_length = len(Content_List)
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
            key_list = ['(1)', '(2)', '(7)', '(9)', '(10)', '(17)', '(18)', ' +->']



            for key in key_list:
                for index in Content_List:
                    if key in index:
                        if key == '(1)':
                            Unclass = key + ' ' + index[8:16] + '\t'
                            writeVar.write(Unclass)
                        if key == '(2)':
                            Ground = key + ' ' + index[8:16] + '\t'
                            writeVar.write(Ground)

                        if key == '(7)':
                            Noise = key + ' ' + index[8:16] + '\t'
                            writeVar.write(Noise)

                        if key == '(9)':
                            Water = key + ' ' + index[8:16] + '\t'
                            writeVar.write(Water)
                        if key == '(10)':
                            Ignored_Ground = key + ' ' + index[8:16] + '\t'
                            writeVar.write(Ignored_Ground)
                        if key == '(17)':
                            BridgeDecks = key + ' ' + index[8:16] + '\t'
                            writeVar.write(BridgeDecks)
                        if key == '(18)':
                            HighNoise = key + ' ' + index[8:16] + '\t'
                            writeVar.write(HighNoise)
                        if key == ' +->':
                            Points_Withheld = key + ' ' + index[25:35] + '\n'
                            writeVar.write(Points_Withheld)
                            


                        
                        print filename, key, index
                        
                """if '(1)' in index:
                    Unclass = index[8:16] + '\t'                 
                    writeVar.write(Unclass)
                    
                    
                elif '(1)' not in Content_List:
                    Unclass = 'None' + '\t'
                    writeVar.write(Unclass)
                    
                elif '(2)' in index:
                    Ground = index[8:16] + '\t'
                    writeVar.write(Ground)
                    
                elif '(2)' not in index:
                    Ground = 'None' + '\t'
                    writeVar.write(Ground)

                    
                elif '(7)' in index:
                    Noise = index[8:16] + '\t'
                    writeVar.write(Noise)       
                elif '(7)' not in index:
                    Noise = ' ' + '\t'
                    writeVar.write(Noise)

                    
                elif '(9)' in index:
                    Water = index[8:16] + '\t'
                    writeVar.write(Water)
                elif '(9)' not in index:
                    Water = 'None' + '\t'
                    writeVar.write(Water)
            
                elif '(10)' in index:
                    Ignored_Ground = index[8:16] + '\t'
                    writeVar.write(Ignored_Ground)
                    
                elif '(10)' not in index:
                    Ignored_Ground = 'None' + '\t'
                    writeVar.write(Ignored_Ground)
                    
                elif '(17)' in index:
                    BridgeDecks = index[8:16] + '\t'
                    writeVar.write(BridgeDecks)
                    
                elif '(17)' not in index:
                    BridgeDecks = 'None' + '\t'
                    writeVar.write(BridgeDecks)
                    
                elif '(18)' in index:                  
                    High_Noise = index[8:16] + '\t'
                    writeVar.write(High_Noise)    
                elif '(18)' not in index:
                    High_Noise = 'None' + '\t'
                    writeVar.write(High_Noise)
                        
                        
                elif ' +->' in index:    
                    Points_Withheld = index[25:35] + '\n'
                    writeVar.write(Points_Withheld)
                elif ' +->' not in index:
                    Points_Withheld = 'None' + '\n'
                    writeVar.write(Points_Withheld)"""

            

            
            #delete the temporary data in the Content_List variable so that it is an empty list for the next iteration"""
            del Content_List[:]
           
            

            
writeVar.close()






