def traverse(alist):
    index = 0
    for word in alist:
        x = len(alist[index])
        index += 1
        print x,

x = ["spam!", "one", ["Brie", "Roquefort", "Pol le Veq"], [1,2,3]]
traverse(x)
