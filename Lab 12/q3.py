def find(strng, ch, start):
    index = start
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1

def count_letters(word,letter):
    position = 0
    place = ""
    while find(word,letter,position) > -1:
        x = find(word,letter,position)
        place += str(x)
        position = x + 1
    return place
            
    
    
    
