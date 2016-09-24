def remove_extension(name):
    """
    >>> remove_extension("tst.txt")
    'tst'
    >>> remove_extension("tst.txt")
    'tst.2'
    >>> remove_extension("hi.txt")
    'hi'
    """
    extns = ".txt",".png"
    filename = ""
    count = 0
    while count <= len(name):
        for char in name:
            count += 1
            if char not in extns:
                x = filename + char
    return x



if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
    
