def line(a,b):
    z = ""
    for number in b:
        q = a + number
        z += q
    return z
        


def table(x,y):
    grid = ""
    for ch in x:
        grid += line(ch, y), "\n"
    return grid





