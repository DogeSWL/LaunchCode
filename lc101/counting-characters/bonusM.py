def getFactor(num):
    rtnList = []

    for i in range(1,num+1):
        if num % i == 0:
            rtnList.append(i)

    return rtnList

def factors(num):
    facList = {}

    for i in range(1,num+1):
        facList[i] = getFactor(i)

    return facList

def reverse(dictL):
    revDict = {}

    for i in dictL:
        for b in dictL[i]:
            if b not in revDict:
                revDict[b] = [i]
            else:
                revDict[b].append(i)
    return revDict

def main():
    a = input("Choose a number: ")
    b = factors(int(a))
    print(b)
    print(reverse(b))

if __name__ == "__main__":
    main()
