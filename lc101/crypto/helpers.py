def alphabet_position(letter):
    aList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z']

    for num in range(len(aList)):
      if letter == aList[num]:
        return num
      if letter not in aList:
        return letter

def rotate_character(char,rot):
    aList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z']

    letterUpper = True
    posLtr = alphabet_position(char.lower())
    rtnLtr = ""

    if char.isalpha():
      if char.islower():
        letterUpper = False
      if posLtr+rot > 25:
        rtnLtr = aList[posLtr+rot-26]
        if letterUpper:
          return rtnLtr.upper()
        else:
          return rtnLtr
      else:
        rtnLtr = aList[posLtr+rot]
        if letterUpper:
          return rtnLtr.upper()
        else:
          return rtnLtr
    else:
      return char
