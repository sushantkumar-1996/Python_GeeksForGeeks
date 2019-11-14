"""Simple Intrest Formula is given by
                            Simple Intrest= (P*T*R)/100
                            P-Principle Amount, T-Time, R-Rate
"""

P = int(input("Enter Principal Amount"))
T = float(input("Enter Time"))
R = float(input("Enter Rate Of Intrest"))

SI = (P*T*R) / 100
print(SI)


"""Compound Intrest Formula is Given By
                Compound  Intrest=P((1+R)/100)^T
                P-Principal, R-Rate, T -time Span
"""

P1 = int(input("Enter Principal Amount"))
T1 = float(input("Enter Time"))
R1 = float(input("Enter Rate Of Intrest"))

CI = P1 * (pow((1 + R1 / 100), T1))
print(CI)