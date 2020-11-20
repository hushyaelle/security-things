import sys

string = str(sys.argv[1])
ascii_list = []
temp_list = list(string)

for i in temp_list:
    ascii_list.append(ord(i))
print(ascii_list)