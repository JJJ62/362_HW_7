
def is_leapyear(year):
    if(int(year) % 4 == 0):
        if(int(year) % 100 == 0):
            if(int(year) % 400 == 0):
                print(str(year) + " is a leap year\n")
                return 1
            else:
                print(str(year) + " is not a leap year\n")
                return 0
        else:
            print(str(year) + " is a leap year\n")
            return 1
    else:
        print(str(year) + " is not a leap year\n")
        return 0
