def new_line():
    print
    
def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    nine_lines()
    nine_lines()
    nine_lines()
    nine_lines()
    three_lines()
    print


print "first line"
clear_screen()    
print "second line"    
