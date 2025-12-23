n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
mx = a[0][0]
ind1 = 0
ind2 = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > mx:
            mx = a[i][j]
            ind1 = i
            ind2 = j
print(ind1, ind2)