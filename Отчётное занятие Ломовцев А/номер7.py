n=int(input())
if n<1:
    n==1
elif n>9:
    n=9
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
