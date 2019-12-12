"""Python Program to generate a Random number--- For this purpose we will be using randint() function which belongs in random
module which can be found in python tutorials section"""

import random
a = int(input("Enter Lower Limit of Random number"))
b = int(input("Enter Upper Limit of Random number"))
print(random.randint(a, b))  # This Function generates random number between a and b inclusive of a and b
