from random import randint
n,m=map(int,input().split())
A=[[0]*m for x in range(n)]
maxi=-1
f=0
for i in range(n):
    for j in range(m):
        A[i][j]=randint(0,9)
        if A[i][j]>maxi:
            maxi=A[i][j]
for row in A:
    print(' '.join(map(str, row)))
for i in range(n):
    for j in range(m):
        if A[i][j]==maxi:
            print(i,j)
            f=1
            break
    if f==1:
        break
