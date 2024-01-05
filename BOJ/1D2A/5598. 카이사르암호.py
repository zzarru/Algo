code = input()

for i in code:
    askii = ord(i) - 3
    if askii < 65:
        letter = chr(90-(64-askii))
    else:
        letter=chr(askii)

    print(letter, end='')