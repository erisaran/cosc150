def function(filename, x):
    op = open(filename)
    read = op.read()
    counter = 1
    while counter <= len(read):
        for char in read:
            if counter % x == 0:
                print char,
            counter += 1
     
        
            
            
        
