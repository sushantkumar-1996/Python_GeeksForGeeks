"""Python Program for converting celsius to fahrenheit or vice versa---- we will use the formula celsius * 1.8 = fahrenheit - 32
"""
cel = float(input("Enter Celsius value"))


def c_to_f(cel):
    return (cel * 1.8) + 32


print(c_to_f(cel))

feh = float(input("Enter fehrenheit value"))


def f_to_c(feh):
    return (feh - 32) / 1.8


print(f_to_c(feh))
