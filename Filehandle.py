def readFile(filename):
    file =open(filename,'r')
    for name in file:
        print(name)
    file.close()
readFile('File.txt')


def readFile2(filename):
    with open(filename,'r') as file: #when with option opening file file close not required
        while True:
            line=file.readline()
            if not line:
                break
            print(line)

def writeFile(filename,data):
    with open(filename, 'w') as file:
        file.write(data + '\n')

def appendFile(filename,data):
    with open(filename,'a') as file:
        file.write(data + '\n')
appendFile('File.txt', 'Writing to the file again')