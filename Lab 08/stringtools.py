def remove_letter(letter,string):
    """
    >>> remove_letter("a","apple")
    'pple"
    >>> remove_letter("a", "banana")
    'bnn'
    >>> remove_letter("z","banana")
    'banana'
    >>> remove_letter("i","Mississippi")
    'Msssspp'
    """
    word = ""
    for char in string:
        if not(char == letter):
            word += char
    return word

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

