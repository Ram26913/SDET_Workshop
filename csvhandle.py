import csv

def readDataFromCSV(filename):
    with open(filename,'r') as file:
        reader = csv.reader(file)
        for data in reader:
            print(data)

def writeDataToCSV(filename):
    with open(filename, 'w', newline='') as file:
        writer =csv.writer(file)
        data = [
            ['Name','Age','City'],
            ['Ram','24','Chennai'],
            ['Rithika','5','Chennai'],
            ['Kala','10','Chennai']
        ]
        for row in data:
            writer.writerow(row)
#writeDataToCSV('data.csv')
readDataFromCSV('data.csv')

def writeDataToCSVDict(filename):
    with open(filename, 'w', newline='') as file:
        header=['Name','Age','City']
        writer=csv.DictWriter(file, fieldnames=header)
        data = [
            {'Name':'Ram','Age':'24','City':'Chennai'},
            {'Name':'Rithika','Age':'5','City':'Chennai'},
            {'Name':'Kala','Age':'24','City':'Chennai'}
        ]
        writer.writeheader()
        for row in data:
            writer.writerow(row)
writeDataToCSVDict('data1.csv')