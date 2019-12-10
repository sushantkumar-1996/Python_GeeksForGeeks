"""Python program for cube sum of first n natural numbers---print the sum of series 1^3+2^3+3^3...+n^3 """


def cubesum(n):
    sm = 0
    for i in range(1, n + 1):
        sm += i * i * i
    return sm


n = int(input("Enter the upper limit of n natural numbers"))
print(cubesum(n))

"""Using formula (n(n+1)/2)^2"""


def sumcube(p):
    return (p * (p + 1) / 2) * (p * (p + 1) / 2)


p = int(input("Enter the upper limit of n natural numbers"))
print(sumcube(p))
