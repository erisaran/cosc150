def checker(word):
    p =[]
    count = 0 
    if word not in words:
        print "incorrect"
        y = len(word)
        for item in words:
            if (y-2)<len(item)<(y+2):
                if lettercheck(item,word)>(y-2):
                    p += item,
    a = relevance(p,word)
    print a
    
                    
                


def lettercheck(d,w):
    count = 0
    for char in w:
        if char in d:
            count += 1
    return count
        
def relevance(p,word):
    count = 0
    while count < 1:
        for let in word:
            x = let
            count += 1
    while count <1:
        for letter in p:
            count += 1
            if letter in x:
                return p
            
        
        



myfile = open("/usr/share/dict/words","r")
text = myfile.read()
words = text.split()
x = raw_input("Write: ")
checker(x)
