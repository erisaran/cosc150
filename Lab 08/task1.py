def on_many_lines(a):
    for x in a:
        print x


#Q2- bE AS HAPPY AS POSSIBLE
# BE AS HAPPY AS POSSIBLE
# 2
# True
# True


prefixes = "JKLMNOPQ"
suffix ="ack"
for letter in prefixes:
    if letter == "O" or letter == "Q":
        print letter+"u"+suffix
    else:
        print letter+suffix

def count_letters(string,letter):
    print string.count(letter)


fruit = "banana"
count = 0
for char in fruit:
    if char == "a":
        count += 1
print count

