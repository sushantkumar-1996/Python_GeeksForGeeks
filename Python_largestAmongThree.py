"""Python program to find largest among three numbers"""

n1 = int(input("Enter First Number"))
n2 = int(input("Enter Second Number"))
n3 = int(input("Enter Third Number"))

if n1 > n2:
    if n1 > n3:
        print("{0} is largest".format(n1))
    elif n3 > n1:
        print("{0} is largest".format(n3))
elif n2 > n3:
    if n2 > n1:
        print("{0} is largest".format(n2))
    elif n1 > n2:
        print("{0} is largest".format(n1))
elif n1 > n3:
    if n1 > n2:
        print("{0} is largest".format(n1))
    elif n2 > n1:
        print("{0} is largest".format(n2))
else:
    print("{0} is largest".format(n3))
