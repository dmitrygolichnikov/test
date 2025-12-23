a=list(map(int,input().split()))
for i in range(len(a)):
    if min(a)%2==0:
        a.pop(a.index(min(a)))
    else:
        print(min(a))
        break
if len(a)==0:
    print(0)