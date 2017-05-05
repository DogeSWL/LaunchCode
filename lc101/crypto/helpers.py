def alphabet_position(letrNum):
    aList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z']

    # if letrNum is a number, returns a letter
    if isinstance(letrNum,int):
        return aList[letrNum]
    # if letrNum is a letter, returns a number
    if letrNum.isalpha():
        for num in range(len(aList)):
            if letrNum == aList[num]:
                return num
    # if letrNum is not in aList, return letrNum
    if letrNum not in aList:
        return letrNum

def rotate_character(char,rot):

    letterUpper = True
    letr_Pos = alphabet_position(char.lower())
    rtnLtr = ""

    # checks if char is alphabetic characters only
    if char.isalpha():
        # checks if string is lowercase, if True set letterUpper to False
        if char.islower():
            letterUpper = False
        if letr_Pos+rot > 25:
            rtnLtr = alphabet_position(letr_Pos+rot-26)
            if letterUpper:
                return rtnLtr.upper()
            else:
                return rtnLtr
        else:
            rtnLtr = alphabet_position(letr_Pos+rot)
            if letterUpper:
                return rtnLtr.upper()
            else:
                return rtnLtr
    else:
      return char
