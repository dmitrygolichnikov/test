def ispr(n):
    if (n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0) and n != 2 and n!=3 and n!=5 and n!=7:
        return False
    else:
        return True
x = int(input())
if ispr(x):
    print('YES')
else:
    print('NO')