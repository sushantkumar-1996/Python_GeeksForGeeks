"""Area Of circle= pi * (r*r)   Where r= radius of the circle"""


def findarea(radius):
    pi = 3.142
    return pi * (radius * radius)


radius = int(input("Enter Radius of circle"))
print("Area Of circle is:", findarea(radius))


