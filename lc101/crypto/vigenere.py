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

print(encrypt('no where', 'boom'))
