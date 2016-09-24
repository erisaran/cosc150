def is_even(n):
    if n%2==0:
        return True
    else:
        return False
        
def is_odd(n):
    if n%2==0:
        print "False"
    else:
        print "True"

def is_factor(n1,n2):
    x=n2%n1
    if x==0:
        print "True"
    else:
        print "False"

def hypotenuse(a,b):
    if a<=0 or b<=0:
        print "sides need to have a positive length"
        return
    x=(a**2)+(b**2)
    h=x**(0.5)
    print h

