from math import *
n = float(input())
if n-int(n) < 0.5:
    print(int(n))
else:
    print(ceil(n))