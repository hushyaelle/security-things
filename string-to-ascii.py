import sys

string = str(sys.argv[1])
length = len(string)
ascii_list = []
l = 0

# split string into a list and convert the characters
while l < length:
    letter = string[l]
    ascii_list.append(ord(letter))
    l = l+1
print(ascii_list)