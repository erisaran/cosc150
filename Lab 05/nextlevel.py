def next_level(a,b,c,d,e,f):
    x= (a+b+c+d+e+f) - min(a,b,c,d,e,f)
    if x<200:
        print "Repeat"
    if x>=200:
        print "Pass"
