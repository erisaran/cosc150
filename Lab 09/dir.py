import os

myfile = raw_input('enter directory or file name')
if myfile == os.path.isdir("s"):
    print os.listdir(myfile)
else:
    x = open(myfile)
    read = x.read()
    print read
    
