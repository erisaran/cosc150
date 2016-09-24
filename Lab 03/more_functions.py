def powers(n):
    print "The first 5 powers of",n,"are", n**0,n**1,n**2,n**3,n**4

def score_summary(name,a,b,c):
    print name, ":", "max",max (a,b,c),"min", min (a,b,c),"average", (a+b+c)/3
    
def signature():
    print "Humphrey Hopalong"

def reject(name):
    print "Dear",name
    print "I am sorry to inform you that you do not have the job"
    print "Yours sincerely"
    print signature()

def accept(name):
    print "Dear",name
    print "I am pleased to inform you that you have the job"
    print "Yours sincerely"
    print signature()

def show_first(a,b,c,d):
    print min(a,b,c,d)
    

