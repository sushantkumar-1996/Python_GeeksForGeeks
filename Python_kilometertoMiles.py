"""Python Program to Convert kilometers to miles---- user enters the distance in kilometers or miles and the program converts it into
Corresponding kilometers or miles"""

conv_fac = 0.6231
km = float(input("Enter values in kilometers"))


def km_ml(km):
    return km * conv_fac


print(km_ml(km))

ml = float(input("Enter value in miles"))


def ml_km(ml):
    return ml / conv_fac


print(ml_km(ml))
