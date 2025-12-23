a = list(map(int, input().split()))
ctn = 0
mn = a[0]
for el in a:
    if el%2 != 0:
        ctn += 1
        if el < mn or mn%2 == 0:
            mn = el
if ctn == 0:
    print(ctn)
else:
    print(mn)