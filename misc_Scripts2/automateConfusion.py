import os, shutil, string, sys

NonVegFile = open(r'D:\2016_ClarkCounty_imageryclassification\FinalAccuracy_Stats\Dataset_12_28_2017\NonVeg.txt', 'r')
turf = open(r'D:\2016_ClarkCounty_imageryclassification\FinalAccuracy_Stats\Dataset_12_28_2017\turf.txt', 'r')
tree = open(r'D:\2016_ClarkCounty_imageryclassification\FinalAccuracy_Stats\Dataset_12_28_2017\Tree.txt', 'r')

def countVeg(vegFile):
    Veg_Lines = vegFile.readlines()
    NonVeg_class = 0
    tree_class = 0
    turf_class = 0
    container = {}
    for line in Veg_Lines:
        val = 0
        if line.split(',')[3][:-1].isdigit():
            val = int(line.split(',')[3][:-1])
            if val == 0:
                NonVeg_class += 1
            elif val ==1:
                tree_class += 1
            elif val == 3:
                turf_class += 1
    container['nonveg'] = NonVeg_class
    container['tree'] = tree_class
    container['turf'] = turf_class
    return container

def calcStats(file1, file2, file3):
    NonVeg_row1 = file1['nonveg'] + 1.0
    turf_row2 = file2['turf'] + 1.0
    tree_row3 = file3['tree'] + 1.0


    
    row1_total = file1['turf'] + file1['tree'] + NonVeg_row1
    row2_total = turf_row2 + file2['tree'] + file2['nonveg']
    row3_total = file3['turf'] + tree_row3 + file3['nonveg']
    sumTotal = row1_total + row2_total + row3_total
    overallAcc = ((NonVeg_row1 + turf_row2 + tree_row3)/float(sumTotal))
    col1_total = NonVeg_row1 + file2['nonveg'] + file3['nonveg']
    col2_total = turf_row2 + file1['turf'] + file3['turf']
    col3_total = tree_row3 + file1['tree'] + file2['tree']
    
    kappa = ((float(sumTotal)*(float(NonVeg_row1) + float(turf_row2) + float(tree_row3)))-((col1_total*row1_total) \
                                                                                           +(col2_total*row2_total)+(col3_total*row3_total)))/((sumTotal**2)-((col1_total * row1_total)+(col2_total * row2_total)+(col3_total*row3_total)))
 
    ReturnStats = {}
    ReturnStats['Overall'] = overallAcc
    ReturnStats['Kappa'] = kappa
    ReturnStats['col1'] = col1_total
    ReturnStats['col2'] = col2_total
    ReturnStats['col3'] = col3_total
    ReturnStats['sumTotal'] = sumTotal


    return ReturnStats

def GroundTruth(file1, file2, file3):
    NonVeg_row1 = file1['nonveg'] + 1
    turf_row2 = file2['turf'] + 1
    tree_row3 = file3['tree'] + 1

    row1_total = file1['turf'] + file1['tree'] + NonVeg_row1
    row2_total = turf_row2 + file2['tree'] + file2['nonveg']
    row3_total = file3['turf'] + tree_row3 + file3['nonveg']

    matrix = [['NonVeg', 'Turf', 'Tree'],['NonVeg', NonVeg_row1/float(row1_total), file1['turf']/float(row1_total), file1['tree']/float(row1_total)], \
              ['Turf', file2['nonveg']/float(row2_total), file2['turf']/float(row2_total), file2['tree']/float(row2_total)], ['Tree', file3['nonveg']/float(row3_total), file3['turf']/float(row3_total), file3['tree']/float(row3_total)]]
    return matrix

def Errors(file1, file2, file3):
    NonVeg_row1 = file1['nonveg'] + 1.0
    turf_row2 = file2['turf'] + 1.0
    tree_row3 = file3['tree'] + 1.0


    CommissionError = {}
    OmissionError = {}
    
    CommissionError['NonVeg'] = (file2['nonveg'] + file3['nonveg'])/float(NonVeg_row1 + file2['nonveg'] + file3['nonveg'])
    CommissionError['Turf'] = (file1['turf'] + file3['turf'])/float(turf_row2 + file1['turf'] + file3['turf'])
    CommissionError['Tree'] = (file1['tree'] + file2['tree'])/float(tree_row3 + file1['tree'] + file2['tree'])

    OmissionError['NonVeg'] = (file1['turf'] + file1['tree'])/float(file1['turf'] + file1['tree'] + NonVeg_row1)
    OmissionError['Turf'] = (file2['nonveg'] + file2['tree'])/float(turf_row2 + file2['tree'] + file2['nonveg'])
    OmissionError['Tree'] = (file3['nonveg'] + file3['turf'])/float(file3['turf'] + tree_row3 + file3['nonveg'])
    
    returnTuple = (CommissionError, OmissionError)
    
    return returnTuple


def UserProducerAcc(file1, file2, file3):
    NonVeg_row1 = file1['nonveg'] + 1.0
    turf_row2 = file2['turf'] + 1.0
    tree_row3 = file3['tree'] + 1.0

    col1_total = NonVeg_row1 + file2['nonveg'] + file3['nonveg']
    col2_total = turf_row2 + file1['turf'] + file3['turf']
    col3_total = tree_row3 + file1['tree'] + file2['tree']

    row1_total = file1['turf'] + file1['tree'] + NonVeg_row1
    row2_total = turf_row2 + file2['tree'] + file2['nonveg']
    row3_total = file3['turf'] + tree_row3 + file3['nonveg']

    ProdAcc = {}
    UserAcc = {}
    
    ProdAcc['NonVeg'] = NonVeg_row1/float(col1_total)
    ProdAcc['Turf'] = turf_row2/float(col2_total)
    ProdAcc['Tree'] = tree_row3/float(col3_total)

    

    UserAcc['NonVeg'] = NonVeg_row1/float(row1_total)
    UserAcc['Turf'] = turf_row2/float(row2_total)
    UserAcc['Tree'] = tree_row3/float(row3_total)
    
   
    
    returnTuple = (UserAcc, ProdAcc)
    
    return returnTuple
    
    

NonVeg =  countVeg(NonVegFile)
turf = countVeg(turf)
tree = countVeg(tree)

stats = calcStats(NonVeg, turf, tree)
print NonVeg
print tree
print turf
Overall_Acc = stats['Overall']
Kappa = stats['Kappa']
print Overall_Acc
print Kappa

ground = GroundTruth(NonVeg, turf, tree)

ErrorReport = Errors(NonVeg, turf, tree)
print ErrorReport[0]['NonVeg']



userprod = UserProducerAcc(NonVeg, turf, tree)
print userprod[1]['Tree']


outputFile = open(r'D:\TestAcc.csv','w')

outputFile.write(",NonVeg,Turf,Tree,\n")
outputFile.write('NonVeg'+ ',' + str(NonVeg['nonveg'] + 1) + ',' + str(NonVeg['turf']) + ',' + str(NonVeg['tree']) + ',' + str(NonVeg['nonveg'] + NonVeg['turf'] + NonVeg['tree'] + 1) + '\n')
outputFile.write('Turf' + ',' + str(turf['nonveg']) + ',' + str(turf['turf'] + 1) + ',' + str(turf['tree']) + ',' + str(turf['nonveg'] + turf['turf'] + turf['tree'] + 1) + '\n')
outputFile.write('Tree' + ',' + str(tree['nonveg']) + ',' + str(tree['turf']) + ',' + str(tree['tree'] + 1) + ',' + str(tree['nonveg'] + tree['turf'] + tree['tree'] + 1) + '\n')
outputFile.write("" + ',' + str(stats['col1']) + ',' + str(stats['col2']) + ',' + str(stats['col3']) + ',' + str(stats['sumTotal']) + '\n')
outputFile.write('\n')
outputFile.write('\n')
outputFile.write('overall accuracy' + ',' + str(stats['Overall']) + '\n')
outputFile.write('Kappa' + ',' + str(stats['Kappa']) + '\n')
outputFile.write('\n')
outputFile.write('\n')
outputFile.write("" + ',' + ground[0][0] + ',' + ground[0][1] + ',' + ground[0][2] + '\n')
outputFile.write(ground[1][0] + ',' + str(ground[1][1]) + ',' + str(ground[1][2]) + ',' + str(ground[1][3]) + '\n')
outputFile.write(ground[2][0] + ',' + str(ground[2][1]) + ',' + str(ground[2][2]) + ',' + str(ground[2][3]) + '\n')
outputFile.write(ground[3][0] + ',' + str(ground[3][1]) + ',' + str(ground[3][2]) + ',' + str(ground[3][3]) + '\n')
outputFile.write('\n')
outputFile.write('\n')
outputFile.write('Commission Error' + ',' + '\n')
outputFile.write('NonVeg' + ',' + str(ErrorReport[0]['NonVeg']) + '\n')
outputFile.write('turf' + ',' + str(ErrorReport[0]['Turf']) + '\n')
outputFile.write('tree' + ',' + str(ErrorReport[0]['Tree']) + '\n')
outputFile.write('\n')
outputFile.write('\n')
outputFile.write('Omission Error' + ',' + '\n')
outputFile.write('NonVeg' + ',' + str(ErrorReport[1]['NonVeg']) + '\n')
outputFile.write('turf' + ',' + str(ErrorReport[1]['Turf']) + '\n')
outputFile.write('tree' + ',' + str(ErrorReport[1]['Tree']) + '\n')
outputFile.write('\n')
outputFile.write('\n')
outputFile.write('Producer Accuracy' + ',' + '\n')
outputFile.write('NonVeg' + ',' + str(userprod[1]['NonVeg']) + '\n')
outputFile.write('turf' + ',' + str(userprod[1]['Turf']) + '\n')
outputFile.write('tree' + ',' + str(userprod[1]['Tree']) + '\n')
outputFile.write('\n')
outputFile.write('\n')
outputFile.write('User Accuracy' + ',' + '\n')
outputFile.write('NonVeg' + ',' + str(userprod[0]['NonVeg']) + '\n')
outputFile.write('turf' + ',' + str(userprod[0]['Turf']) + '\n')
outputFile.write('tree' + ',' + str(userprod[0]['Tree']) + '\n')





outputFile.close()
