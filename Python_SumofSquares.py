"""Python program for sum of squares of first n natural numbers-----Given a positive integer N the task is to find 1^2+2^2+3^2...+N^2"""


# Method 1--O(n)-- run a loop from 1 to n and for each i, 1<=i<=n, find i^2 to sum

def sumsqr(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i)
    return sm


n = int(input("Enter the First n natural number uper limit"))
print(sumsqr(n))

"""Sum of first N natural numbers--N*(N+1)*(2*N+1)/6"""


def sqrsum(p):
    return (p * (p + 1) * (2 * p + 1)) // 6


p = int(input("Enter the First n natural number upper limit"))
print(sqrsum(p))
