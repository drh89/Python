import csv
import os



os.chdir('C:\\Users\Runej\Desktop\\')


def printFileContent(file):
    with open(file, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            print(row)


    
#printFileContent('Test.csv')

tuples = [('banana', 'apple', 'orange'), ('Rune', 'Dennis', 'Arne')]


def writeListToFile(outputFile, lst):
    with open(outputFile, 'w') as f:
        
        for x in lst:
        
            listToCopy = ''.join(str(x) + '\n')
            f.write(listToCopy)

#writeListToFile('Test2.txt', tuples)

def writeListToFileString(outputFile, lst):
    with open(outputFile, 'w') as f:
        
        for x in lst:
            for y in x:
        
                listToCopy = ''.join(str(y) + '\n')
                f.write(listToCopy)

#writeListToFileString('Test2.txt', tuples)

def readCsv(inputFile):
    res = []
    with open(inputFile, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            res.append(str(row) + '\n')
        print(str(res))

readCsv('Test.csv')