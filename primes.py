def is_prime(x):
    """
    >>> is_prime(2)
    True
    >>> is_prime(9)
    False
    >>> is_prime(4)
    False
    """
    count = 0
    y = x - 1
    while y>1:
        if x%y > 0:
            count += 1
        y = y-1
    if count == x-2:
        return True
    else:
        return False
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    
