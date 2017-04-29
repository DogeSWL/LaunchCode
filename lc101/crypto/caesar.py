def alphabet_position(letter):
    # a-z -> 97-122
    # A-Z -> 65-90
    asciiValue = ord(letter)

    return asciiValue

def rotate_character(char, rot):
    a = alphabet_position(char)

    if char.isupper():
        if a+rot > 90:
            return chr((a+rot-90)+64)
        else:
            return chr(a+rot)
    if char.islower():
        if a+rot > 122:
            return chr((a+rot-122)+96)
        else:
            return chr(a+rot)
    else:
        return chr(a)

def encrypt(text, rot):
    rtnText = ""

    for i in text:
        rtnText += rotate_character(i,rot)

    return rtnText

def main():
    a = input("Type a message:")
    b = input("Rotate by:")
    print(encrypt(a,b))

if __name__ == "__main__":
    main()
