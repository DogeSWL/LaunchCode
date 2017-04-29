def alphabet_position(letter):
    aList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z']

    for i in range(len(aList)):
        if letter == aList[i]:
            return i
    else:
        return letter

def rotate_character(char,rot):
    aList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z']

    letterUpper = True
    rtnLtr = 0

    if char.isalpha():
        if char.islower():
            letterUpper = False

        posL = alphabet_position(char.lower())

        if posL+rot > 25:
            rtnLtr = aList[(posL+rot-26)]
            if letterUpper:
                return rtnLtr.upper()
            else:
                return rtnLtr
        else:
            rtnLtr = aList[(posL+rot)]
            if letterUpper:
                return rtnLtr.upper()
            else:
                return rtnLtr
    else:
        return char
