def num_unique(a_list):
    """
    >>> num_unique([1, 2])
    2
    >>> num_unique([1, 2, 2, 2, 1, 2, 1, 2, 2, 1])
    2
    >>> num_unique([1, 1, 1, 1, 1])
    1
    >>> num_unique([1, 2, 3, 4, 5])
    5
    """
    x = set(a_list)
    return len(x)



if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
