from helpers import alphabet_position, rotate_character

def encrypt(text,rotKey):
    rotKey_str = ''
    keyCount = 0
    rtnText = ""

    # give us rotKey_str with rotKey inputs
    for i in text:
        if i != ' ':
            if keyCount >= len(rotKey):
                keyCount = 0

            rotKey_str += rotKey[keyCount]
            keyCount += 1
        else:
            rotKey_str += i

    for b in range(len(text)):
        rtnText += rotate_character(text[b], alphabet_position(rotKey_str[b]))

    return rtnText

# print(encrypt("The crow flies at midnight!", "boom"))

def main():
    from sys import argv, exit
    if any(str.isdigit(i) for i in argv[1]) == True:
        print("Key should not be an number or special character, should be a character or string of characters")
        exit()
    else:
        inA = input('Type a message: ')
        print(encrypt(inA, argv[1]))

if __name__ == '__main__':
    main()
