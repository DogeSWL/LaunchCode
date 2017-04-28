def get_initials(fullname):
    rtnInitals = ""
    a = fullname.split()

    for i in a:
        rtnInitals+= i[0].upper()

    return rtnInitals


def main():
    a = input()
    print(get_initials(a))

if __name__ == '__main__':
    main()
