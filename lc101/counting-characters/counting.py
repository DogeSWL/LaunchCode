def countAll_Char(text):
    charList = {}

    textList = list(text)

    for lettr in textList:
        if lettr not in charList:
            charList[lettr] = 1
        else:
            charList[lettr] += 1

    for ansOut in charList:
        print(ansOut+":", charList[ansOut])


def main():
    a = input("Please input sentence: ")
    countAll_Char(a)
if __name__ == "__main__":
    main()

#countAll_Char("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus.")
