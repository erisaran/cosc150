def number(filename, word):
    """
    >>> number("anthem.txt", "defend")
    2
    >>> number("anthem.txt", "God")
    3
    """
    myfile = open(filename)
    text = myfile.read()
    wordlist = text.split()
    count = 0
    for words in wordlist:
        if words == word:
            count += 1
    return count

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
