def count_apluses(filename):
    myfile = open(filename)
    numbers = myfile.read()
    marks = numbers.split()
    for n in marks:
        x = int(n)-89
        if x >0:
            print n,
        
        
        
        
