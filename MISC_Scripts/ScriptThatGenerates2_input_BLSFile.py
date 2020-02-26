import os

inputPath =r"H:/PCA_Images/batchFile_2Input.bls"


ThematicRaster_ws = r"E:/ENVI_FeatureExtraction/FeatureAnalyst_test/Trial5/random/raster_firstrountModels"

Binary_ws = r"E:/ENVI_FeatureExtraction/test_imagery/DMCII/Binary_Imagery"


outFile = open(inputPath, "w")
outFile.write("Input1\tInput2\n")
ThematicRaster_List = []
Binary_List = []



for root, dirs, files in os.walk(ThematicRaster_ws):
    for filename in files: 
        if filename[-4::1] == '.img':
            ThematicRaster_Line = '"{ThematicWorkSpace}/{Thematic_file}"'.format(ThematicWorkSpace = ThematicRaster_ws, Thematic_file = filename)
            ThematicRaster_List.append(ThematicRaster_Line)

for root, dirs, files in os.walk(Binary_ws):
    for FName in files:
        if FName[-4::1] == ".img":
            Binary_Line = '"{BinaryWorkSpace}/{image}"'.format(BinaryWorkSpace = Binary_ws, image = FName)
            Binary_List.append(Binary_Line)

ListCount = len(ThematicRaster_List)
for i in range(0, ListCount):
    line = ThematicRaster_List[i]+'\t'+ Binary_List[i]+'\n'
    outFile.write(line)
outFile.close()    





