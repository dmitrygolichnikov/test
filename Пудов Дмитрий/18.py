def Isascending(a):
    k=1
    dlina = len(a)
    respect=False
    while a[k-1]<a[k] and  k!=dlina-1:
        k+=1
    if k==dlina-1:
        respect=True
    return respect

if Isascending(list(map(int,input().split())))==True:
    print("YES")
else:
    print('NO')