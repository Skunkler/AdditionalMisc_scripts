import os, sys, string, shutil

input1_ws = raw_input("please enter a workspace")

QL = raw_input("Please enter a QL Level for info files: ")

writeVar = open(input1_ws + '\\compiled_lasinfo.txt', 'w')

writeVar.write('ID\tQL\tLast\tDensity(Last)\tSpacing(Last)\tMin_Elevation\tMax_Elevation\tUnclass\tGround\tWithheld\n')


def reserveSplit(dictLine, keyWordObj):
    reserveStr = dictLine
    outNum = ''
    for i in reserveStr.split(keyWordObj)[0]:
        if i.isdigit():
            outNum += i
    return outNum

def unclassedPoints(dictLine):
    unclassStr = dictLine
    outUnClass = ''
    for i in dictLine.split('unclassified')[0]:
        if i.isdigit():
            outUnClass += i
    return outUnClass

def groundClass(dictLine):
    groundStr = dictLine
    outGround = ''
    for i in dictLine.split('ground')[0]:
        if i.isdigit():
            outGround += i
    return outGround


def getlastReturns(dictline):
    lastReturnNum = ''
    for i in dictline.split('returns:')[1]:
        if i.isdigit():
            lastReturnNum += i
    return lastReturnNum

def getPointDensities(dictline):
    outlist = []
    for word in dictline.split(' '):
        if word[0].isdigit():
            outlist.append(word)
    
    return outlist[1]

def getSpacingDensities(dictline):
    SpacingList = []
    for word in dictline.split(' '):
        if len(word) > 0 and word[0].isdigit():
            SpacingList.append(word)
    return SpacingList





for root, dirs, files in os.walk(input1_ws):
    for filename in files:
        if filename[-9:] == '_info.txt':
            Table_Key = filename[0:5] + '.las'
            #print Table_Key
            
            InfoFile_loc = input1_ws + '\\' + filename
            infofile = open(InfoFile_loc, 'r')

            lines = infofile.readlines()
            #print Table_Key, len(lines)
            line_with = dict_input['withheld_' + Table_Key] = lines
            Reserved = 'Reserved'
            unclassified = 'unclassified'
            ground = 'ground'
            noise = 'noise'
            water = 'water'
            rail = 'rail'
            bridge = 'bridge deck'
            minElev = 'min x y z'
            maxElev = 'max x y z'
            lastReturns = 'last returns'
            pointDensity = 'point density:'
            pointSpacing = 'spacing:'

            minElev_list = []
            maxElev_list = []
            lastReturn_list = []
            pointDensity_list = []
            spacing_list = []
            unclass_list = []
            ground_list = []
            reserved_list = []
            
            for i in range(0, len(lines)):
                
                    
                if minElev in lines[i]:
                    minElevValue = lines[i].split(' ')[-1][:-1]
                    

                if maxElev in lines[i]:
                    maxElevValue = lines[i].split(' ')[-1][:-1]

                if lastReturns in lines[i]:
                    lastReturnsVal = getlastReturns(lines[i])
                    

                if pointDensity in lines[i]:
                    pointDensityValue = Table_Key, getPointDensities(lines[i])

                if pointSpacing in lines[i]:
                    Spacing = getSpacingDensities(lines[i])
                   
                    
                if unclassified in lines[i]:
                    unStr = reserveSplit(lines[i], unclassified)
                    
                    
                if ground in lines[i]:
                    strGround = reserveSplit(lines[i], ground)

                if Reserved in lines[i]:
                    ReserveNum = reserveSplit(lines[i], Reserved)
                    
                    output_write_line = Table_Key + '\t' + QL + '\t' + lastReturnsVal + '\t' + pointDensityValue[1] + '\t' + Spacing[1] + '\t' + minElevValue + '\t' + maxElevValue + '\t' + unStr + '\t' + strGround + '\t' + ReserveNum + '\n'
                #else:
                #    ReserveNum = ''
                 
                    
            output_write_line = Table_Key + '\t' + QL + '\t' + lastReturnsVal + '\t' + pointDensityValue[1] + '\t' + Spacing[1] + '\t' + minElevValue + '\t' + maxElevValue + '\t' + unStr + '\t' + strGround + '\t' + ReserveNum + '\n'
            
            
            writeVar.write(output_write_line)


writeVar.close()
