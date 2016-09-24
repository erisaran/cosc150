def shape(x):
    if x==1:
        triangle(x,y)
        return
    elif x==2:
        circle(r)
        return
    elif x==3:
        square(h,w)
        return
    else:
        print "Invalid input"

def triangle(x,y):
    x=raw_input("Enter base length: ")
    y=raw_input("Enter height: ")
    area=x*y*0.5
    print area


print "Calculate the area of which shape?"
print "  1 a triangle"
print "  2 a circle"
print "  3 a square"
a=raw_input("Enter a number to choose: ")
shape(a)
