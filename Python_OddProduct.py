"""Python Program for finding a distinct  pair of numbers whose product is odd from a sequence of integer values
"""

def odd_prod(num_arr):
    for i in range(len(num_arr)):
        for j in range(len(num_arr)):
            if i != j:
                prod = num_arr[i] * num_arr[j]
                if prod % 2 == 0:  # We can use if prod & 1:(  To check if odd product is present or not )
                    print(False)
                else:
                    print(True)


num_arr = []
n = int(input("Enter number of elements"))
for i in range(0, n):
    elements = int(input())
    num_arr.append(elements)
print(odd_prod(num_arr))


