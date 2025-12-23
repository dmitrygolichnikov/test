def IsAscending(A):
    s=1
    for i in range(1,len(A)):
        if A[i-1]<A[i]:
            s=s*1
        else:
            s=s*0
    return s
A=list(map(int,input().split()))
d=IsAscending(A)
if d==1:
    print('YES')
else:
    print('NO')
