def ispinsq(x, y):
    return abs(x) <= 1 and abs(y) <= 1
n = float(input())
m = float(input())
if ispinsq(n, m):
    print('YES')
else:
    print('NO')