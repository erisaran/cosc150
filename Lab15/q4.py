def lettercount(string):
    counts = {}
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1
