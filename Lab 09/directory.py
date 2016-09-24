import os
print os.listdir(".")

x = raw_input("enter one of the file names: ")
myfile = open(x)
read = myfile.read()
print read
