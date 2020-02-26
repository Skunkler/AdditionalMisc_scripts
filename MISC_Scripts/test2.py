import os

input1_ws = r"L:\Lidar\_ClarkCounty_2016\Vendor_Products\RAW_LAS_Flightline\RawPointCloud_QL2"
#"L035-1-160424A-C1_r_info.txt"
input2 = r"H:\Lidar_Python_Project\warnings.txt"

QL = "QL2\t"
readWarn = open(input2, 'r')

writeVar = open(input1_ws + '\\Test2.txt', 'w')
writeVar.write("ID\t" + "QL1 or QL2\t" + "Number of last returns\t" + "Point Density(All Returns)\t" + \
                           "Point Density(Last Only)\t" + "Spacing(All Returns)\t" + "Spacing(Last Only)\n")
Content_List = []

for root, dirs, files in os.walk(input1_ws):
    for filename in files:
        if filename[-8::1] == "info.txt":
            Table_Key = filename[-28:-9:1] + '.las' + '\t'
            ReadFile_Name = input1_ws + '\\' + filename
            readVar = open(ReadFile_Name, 'r')
            for i in readVar:
                Content_List.append(i)
            readVar.close()
            Last_Returns = Content_List[47][-15:-1:1] + '\t'
            
            Point_Density1 = Content_List[50][-40:-35:1] + '\t'
            Point_Density2 = Content_List[50][-25:-20:1] + '\t'
            Spacing1 = Content_List[51][-31:-27:1] + '\t'
            Spacing2 = Content_List[51][-16:-12:1] +'\n'

             
            writeVar.write(Table_Key)
            writeVar.write(QL)
            writeVar.write(Last_Returns)
            writeVar.write(Point_Density1)
            writeVar.write(Point_Density2)
            writeVar.write(Spacing1)
            writeVar.write(Spacing2)
            del Content_List[:]
writeVar.close()
readVar.close()
readWarn.close()




