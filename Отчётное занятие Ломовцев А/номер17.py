A=list(map(int,input().split()))
s=0
for i in range(1,len(A)-1):
    if A[i-1]<A[i]>A[i+1]:
        s+=1
print(s)
