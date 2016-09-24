import os, glob, re

photos = glob.glob("/home/cshome/coursework/COMP150/coursefiles150/Photos/*.jpg")

for p in photos:
    newp = re.sub(".*/([a-z_0-9]+)\.jpg", r"\1", p)
    print ("input name: " + p + ", output name: " + newp)
    command = "convert " + p + " -resize 50x50 " + newp + "_50.jpg"
    print ("doing: " + command)
    os.system(command)

print ("Done")
