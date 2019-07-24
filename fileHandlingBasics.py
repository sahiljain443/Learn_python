#Basic file handling operations

def makeFile(fileName, message, mode):
    a = open(fileName, mode)
    a.write(message)
    a.close()
    
def openFile(fileName):
    b = open(fileName, "r")
    lines = b.readlines()
    for line in lines:
        print (line)
    b.close()
    
makeFile("fileFirst.txt","This is my first file 1\n", "w")
makeFile("fileFirst.txt","This is my first file 2\n", "w")
makeFile("fileFirst.txt","This is my first file 3\n", "w")

makeFile("fileSecond.txt","This is my second file 3\n", "a")
makeFile("fileSecond.txt","This is my second file 3\n", "a")
makeFile("fileSecond.txt","This is my second file 3\n", "a")

print("write fileFirst.txt")
print("--------------------")
    
openFile("fileFirst.txt")
print("--------------------")

print("write secondFile.txt")
print("--------------------")
    
openFile("fileSecond.txt")
print("--------------------")
    