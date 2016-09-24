def print_powers(n, high):
    power = 1
    while power <= high:
        print n**power,
        power += 1
        
def x(high):
    i = 1
    while i <= high:
        power = 1
        while power <= high:
            print i**power,
            power += 1
        i += 1
        print ""
    
    
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(9)
    False
    """
    i = 2
    count = 0
    while i < n:
        x = n%i
        if x == 0:
            count += 1
        i += 1
    if count > 0:
        return False
    else:
        return True



def primes(number):
    """
    >>> primes(8)
    1 2 3 5 7
    """
    n = 1
    count = 0
    i = 2
    while n <= number:
        while i < n:
            x = n%i
            if x == 0:
                count += 1
            i += 1
        if count == 0:
            print n,
        n += 1
        count = 0
        i = 2
        
    
    
                
            
    
            






if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
    
