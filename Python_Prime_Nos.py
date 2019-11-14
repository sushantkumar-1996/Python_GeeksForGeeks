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


start = int(input("Enter lower interval"))
end = int(input("Enter Upper Interval"))
print(findPrimeInInterval(start, end))
