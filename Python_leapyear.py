"""Python program to determine if the year entered is a leap year or not----- the logic for leap year is that if the year is ivisible
by 4, 100, 400 then it is a leap year along with a few more conditions"""


year = int(input("Enter the year to be checked"))


def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))


print(isLeapYear(year))