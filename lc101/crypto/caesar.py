from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    rtnText = ""

    for i in text:
        rtnText += rotate_character(i,rot)

    return rtnText

def main():
    from sys import argv
    a = input("Type a message: ")
    print(encrypt(str(a),int(argv[1])))

if __name__ == "__main__":
    main()
