def sumof(n):
    """
    >>> sumof(1)
    1
    >>> sumof(9)
    81
    >>> sumof(11)
    2
    >>> sumof(121)
    6
    """
    x = str(n)
    y = 0
    for integer in x:
        y += int(integer)**2
    return y



if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
