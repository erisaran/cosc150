def only_upper(string):
    Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Capitals = ""
    for char in string:
        if char in Upper:
            Capitals += char
    return Capitals

            
