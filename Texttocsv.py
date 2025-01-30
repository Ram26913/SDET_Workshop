import csv
def readFile(filename):
    file =open(filename,'r')
    for name in file:
        print(name)
    file.close()
readFile('File.txt')

def writeDataToCSVDict(filename):
    with open(filename, 'w', newline='') as file:
        for row in name:
            writer.writerow(name)
writeDataToCSVDict('data2.csv')