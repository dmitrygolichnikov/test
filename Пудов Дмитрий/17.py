a=list(map(int,input().split()))
a=[0]+a+[0]
counter=0
for i in range(len(a)-1):
    if a[i-1]<a[i]>a[i+1]:
        counter+=1
print(counter)