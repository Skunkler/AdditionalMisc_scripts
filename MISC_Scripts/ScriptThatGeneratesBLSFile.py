import sys, string, os 

ws = r"H:/ImageDifference_Test/output_hi_images"
inputPath =r"H:/ImageDifference_Test/Buffer_model/Buffer_List.bls"

outFile = open(inputPath, "w")
outFile.write("Input1\n")
for root, dirs, files in os.walk(ws):
    for filename in files: 
        if filename[-4::1] == '.img':
            line = '"{wsPace}/{files}"'.format(wsPace = ws, files = filename)
            lineComplete = line + '\n'
            outFile.write(lineComplete)
outFile.close()
    
