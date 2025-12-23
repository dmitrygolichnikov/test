a=list(map(int,input().split()))
a+='0'
def Isascending(a):
    b=0
    while a[b]<a[b+1] and b!=len(a)-2:
        b+=1
    else:
        return b
        
b=Isascending(a)
if b==len(a)-2:
    print('yes')
else:
    print('no')