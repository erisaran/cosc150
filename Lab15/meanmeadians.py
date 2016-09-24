def mean_median(number_list):
    """
    >>> mean_median([1, 2, 3])
    (2.0, 2.0)
    >>> mean_median([1, 2, 9])
    (4.0, 2.0)
    >>> mean_median([8, 2, 2])
    (4.0, 2.0)
    >>> mean_median([2, 8, 1, 1])
    (3.0, 1.5)
    """
    values = ()
    total = 0.0
    x = 0
    while x < len(number_list):
        total += number_list[x]
        x += 1
    mean = total/len(number_list)
    values +=  (mean),

    return values


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)

    
