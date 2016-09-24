import os, glob

photos = glob.glob("/home/cshome/coursework/COMP150/coursefiles150/Photos/*.jpg")

for p in photos:
    print (p)

print ("Done")
