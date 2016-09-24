def add_lists(a,b):
    """
    >>> add_lists([1, 1], [1, 1])
    [2, 2]
    >>> add_lists([1, 2], [1, 4])
    [2, 6]
    >>> add_lists([1, 2, 1], [1, 4, 3])
    [2, 6, 4]
    >>> list1 = [1, 2, 1]
    >>> list2 = [1, 4, 3]
    >>> sum = add_lists(list1, list2)
    >>> list1 == [1, 2, 1]
    True
    >>> list2 == [1, 4, 3]
    True
    """
    q = []
    count = 0
    for number in a:
        num = b[count]
        x = int(number) + int(num)
        q += x,
        count += 1
    return q



def mult_lists(a,b):
    """
    >>> mult_lists([1, 1], [1, 1])
    2
    >>> mult_lists([1, 2], [1, 4])
    9
    >>> mult_lists([1, 2, 1], [1, 4, 3])
    12
    """
    final = 0
    count = 0
    for number in a:
        num = b[count]
        x = number * num
        final += x
        count += 1
    return final


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
