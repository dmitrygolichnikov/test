number = int(input())

def IsPrime(x):
    if (x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0) or (x == 2 or x == 3 or x == 5 or x == 7):
        return 'YES'
    else:
        return 'NO'

print(IsPrime(number))