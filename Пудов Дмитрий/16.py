a=list(map(int,input().split()))
l=[x for x in a if x%2!=0]
if len(l)==0:
    print(0)
else:
    print(max(l))