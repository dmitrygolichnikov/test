a=list(map(int,input().split()))
def Isascending(a):
    for i in range(len(a)-1):
        if a[i]>=a[i+1]:
            return 'no'
    return 'yes'
b=Isascending(a)
print(b)