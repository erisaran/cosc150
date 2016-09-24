import urllib2

pagefile = urllib2.urlopen("http://www.cs.otago.ac.nz")
page = pagefile.read()
words = page.split()
for word in words:
    if "http" in word:
        print word

