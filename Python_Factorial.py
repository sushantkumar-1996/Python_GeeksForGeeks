# Python Program to find The factorial of a number


def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)


num = int(input("Enter a Number :"))
print("factorial of", num, "is", factorial(num))
