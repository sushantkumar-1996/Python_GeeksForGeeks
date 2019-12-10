"""Python Program for solving Quadratic Equations---program computes roots of quadratic equation when coefficients
a,b,and c are known. Standard form of quadratic equation is ax2 + bx + c = 0, where a,b and c are real numbers and
a ≠ 0"""
#  cmath module is imported to perform complex square root
import cmath
a = int(input("Enter Coeffecient of x^2"))
b = int(input("Enter Coeffecient of x"))
c = int(input("Enter Constant term"))

# Calculating discriminant
d = (b * b) - (4 * a * c)

r1 = (-b-cmath.sqrt(d)) / (2 * a)
r2 = (-b+cmath.sqrt(d)) / (2 * a)

print("The Roots are {0} and {1}".format(r1, r2))