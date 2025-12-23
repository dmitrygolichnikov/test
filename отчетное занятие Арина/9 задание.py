import math

number = float(input())
if number >= 2.5:
    print(math.ceil(number))
else:
    print(int(number))