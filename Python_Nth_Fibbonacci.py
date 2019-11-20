"""Python Program for Nth Fibbonacci Number---- sequence of Fn fibbonacci numbers is defined by the recurrence relation
Fn = Fn-1 + Fn-2 with values F0 = 0,and F1 = 1
"""


# using recursion
def fibbonacci(n):
    if n < 0:
        print("Invalid Input")
    elif n == 1:
        return 0  # as 1 is the first fibbonacci number
    elif n == 2:
        return 1  # as 2 is the second fibbonacci number
    else:
        return fibbonacci(n - 1) + fibbonacci(n - 2)


n = int(input("Enter the Nth Digit "))
print(fibbonacci(n))

# using dynamic programming

fibarray = [0, 1]


def fibbon(x):
    if x < 0:
        print("Invalid Input")
    elif x <= len(fibarray):
        return fibarray[x - 1]
    else:
        tempfib = fibbon(x - 1) + fibbon(x - 2)
        fibarray.append(tempfib)
        return tempfib


x = int(input("Enter the Number"))
print(fibbon(x))


# using dynamic programming with space optimization

def fibbo(y):
    a = 0
    b = 1
    if y < 0:
        print("Incorrect Input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, y):
            c = a + b
            a = b
            b = c
        return b


y = int(input("Enter The nth digit"))
print(fibbo(y))

"""Python program to check if a number is a fibbonacci number--->A number is fibbonacci if and only if one or both of 
 (5*n2 + 4) or (5*n2 – 4) is a perfect square
"""

import math


def isPerfectSquare(q):  # function to check if q is a perfect square
    s = int(math.sqrt(q))
    return s * s == q


def isFibbonacci(w):
    return isPerfectSquare(5 * w * w + 4) or isPerfectSquare(5 * w * w - 4)


for i in range(1, 11):
    if isFibbonacci(i):
        print(i, "is a fibbonacci ")
    else:
        print(i, "is not a fibbonacci")

"""Program for Nth multiple of a number in a fibonacci Series--->>  Example-Input : k = 2, n = 3
Output : 9  3\'rd multiple of 2 in Fibonacci Series is 34  which appears at position 9.
Solution --Fibbonacci series is periodic under modular representation

F (mod 2) = 1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,
            1,1,0,1,1,0,1,1,0,1,1,0,1,1,0 
Here 0 is repeating at every 3rd index and 
the cycle repeats at every 3rd index. 

F (mod 3) = 1,1,2,0,2,2,1,0,1,1,2,0,2,2,1,0
            ,1,1,2,0,2,2,1,0,1,1,2,0,2,2
Here 0 is repeating at every 4th index and 
the cycle repeats at every 8th index.

F (mod 4) = 1,1,2,3,1,0,1,1,2,3,1,0,1,1,2,3,
           1,0,1,1,2,3,1,0,1,1,2,3,1,0 
Here 0 is repeating at every 6th index and 
the cycle repeats at every 6th index.

F (mod 5) = 1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,
            2,2,4,1,0,1,1,2,3,0,3,3,1,4,0
Here 0 is repeating at every 5th index and
the cycle repeats at every 20th index.

F (mod 6) = 1,1,2,3,5,2,1,3,4,1,5,0,5,5,4,
            3,1,4,5,3,2,5,1,0,1,1,2,3,5,2
Here 0 is repeating at every 12th index and 
the cycle repeats at every 24th index.

"""
k = int(input("Enter the number for which we will be finding the multiple"))
h = int(input("Enter the Hth Mltiple of k"))


def findPosition(k, h):
    f1 = 0
    f2 = 1
    j = 2
    while j != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k == 0:
            return n * j
        j += 1
    return


print(findPosition(k, n))
