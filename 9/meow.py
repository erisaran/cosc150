def func(filename, n):
    myfile = open(filename)
    words = myfile.read()
    print words*n


def funct(filename, word):
    myfile = open(filename)
    count = 0
    text = myfile.read()
    wordlist = text.split()
    for x in wordlist:
        if x == word:
            count += 1
    return count



y = open("meow.txt")
z = y.read()
a = z.split()
print a
