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
