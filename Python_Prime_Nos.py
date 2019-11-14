"""Given two positive integer start and end. write a Python program toprint all Prime numbers in an Interval.
Solution Algorithm---- Iterate the Val from Start to End , Check if val >1 , if it divides n(2-n)
"""


def findPrimeInInterval(start, end):
    for val in range(start, end + 1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                print(val)


"""Pytgon Program to Check if a Number is prime or not"""


def checkPrime(num):
    if num == 1:
        print("Number is neither prime nor Composite")
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("Number Not Prime")
                break
        else:
            print("Number is prime")


start = int(input("Enter lower interval"))
end = int(input("Enter Upper Interval"))
num = int(input("Enter Any positive Number"))
print(findPrimeInInterval(start, end))
print(checkPrime(num))
