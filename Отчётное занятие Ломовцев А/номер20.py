n=int(input())
A=[[0]*n for x in range(n)]
for i in range(n):
    for j in range(n):
        if i+j+1==n:
            A[i][j]=1
        if i+j+1>n:
            A[i][j]=2
for row in A:
    print(' '.join(map(str, row)))
