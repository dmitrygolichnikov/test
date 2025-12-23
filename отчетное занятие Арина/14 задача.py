x = int(input())
y = int(input())

def IsPointInSquare(x, y):
    flag = False
    while (x >= -1 and x <= 1) and (y >= -1 and y <= 1):
        flag = True
        break
    return flag


j = IsPointInSquare(x, y)

if j == True:
    print('YES')
else:
    print('NO')