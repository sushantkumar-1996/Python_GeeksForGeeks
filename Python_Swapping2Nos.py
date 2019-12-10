"""Python program to swap two variables-- Basically two methods one by using a temporary variable and one without it
Using a Temporary  Variable---"""

x = int(input("Enter first Number"))
y = int(input("Enter Second Number"))

print("The value of x and y Before swapping is {0} and {1}".format(x, y))

temp = x  # creating a temporary variable and assigning it as same value as x
x = y  # assigning x as same value as y
y = temp  # assigning the temp value to y

print("The value of x and y after swapping is {0} and {1}".format(x, y))

"""Without using Temporary variable"""
a = int(input("Enter first Number"))
b = int(input("Enter Second Number"))

print("The value of a and b Before swapping is {0} and {1}".format(a, b))
a, b = b, a
print("The value of a and b after swapping is {0} and {1}".format(a, b))

"""If the elements to be swapped there aresome other arithmatic logics that can be followed
1.Using Addition And Subtraction
    x = x + y
    y = x - y
    x = x - y

2. Using Multiplication And Division
    x = x * y
    y = x / y
    x = x / y

3. Using XOR(For integers only)
    x = x ^ y
    y = x ^ y
    x = x ^ y
"""

