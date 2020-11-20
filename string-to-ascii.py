def main(string):
    length = len(string)
    character_list = []
    ascii_list = []
    l = 0

    # split string into a list
    while l < length:
        letter = string[l:l+1]
        character_list.append(letter)
        l = l+1

        # covert to ascii characters
        if l >= length:
            for char in character_list:
                ascii_char = ord(char)
                ascii_list.append(ascii_char)

            print(ascii_list)

main("alert(1)")
