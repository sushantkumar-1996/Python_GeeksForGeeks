"""Python program to print multiplication table till any number"""

n1 = int(input("Enter the number for which  multiplication table need to be generated"))
j = int(input("Enter the number uptil which the multiplication table needs to be generated"))

for i in range(1, j+1):
    print(n1, 'x', i, '=', n1 * i)