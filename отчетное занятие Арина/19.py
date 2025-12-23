from random import randint
n,m=map(int,input().split())
a=[[randint(1,100) for i in range(m)] for i in range(n)]
b=a[0][0]
index_i=0
index_j=0
for i in range(n):
    for j in range(m):
        if a[i][j]>b:
            index_i=i
            index_j=j
            b=a[i][j]
print(index_i,index_j)