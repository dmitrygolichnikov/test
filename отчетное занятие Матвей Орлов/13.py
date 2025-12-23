def func(x, y):
    if 1 >= x >= -1 and 1 >= y >= -1:
        return True
    return False

X = int(input())
Y = int(input())

if func(X, Y):
    print('Yes')
else:
    print('No')