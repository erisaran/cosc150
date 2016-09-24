def num_digits(n):
    """
    >>> num_digits(12345)
    5
    >>> num_digits(0)
    1
    >>> num_digits(-12345)
    5
    """
    count = 0
    n = abs(n)
    while n > 0:
        count = count + 1
        n = n/10
    if n == 0 and count == 0:
        count = count + 1
    return count

def num_even_digits(n):
    """
    >>> num_even_digits(123456)
    3
    >>> num_even_digits(2468)
    4
    >>> num_even_digits(1357)
    0
    >>> num_even_digits(2)
    1
    >>> num_even_digits(20)
    2
    """
    count = 0
    while n > 0:
        x = n%10
        if x%2 == 0:
            count += 1
        n = n/10
    return count


            
def print_digits(n):
    """
    >>> print_digits(13789)
    9 8 7 3 1
    >>> print_digits(39874613)
    3 1 6 4 7 8 9 3
    >>> print_digits(213141)
    1 4 1 3 1 2
    """
    while n > 0:
        x = n%10
        print x,
        n = n/10
    return

if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)
    numfile = open("numbers.txt")
    line = numfile.readline()
    while line:
        count = 0
        while line > 0:
            count += 1
            line = int(line) / 10
        print count
        line = numfile.readline()
    numfile.close()
    
