x=int(input())
s=0
for i in range(2,x):
    if x%i==0:
        s+=1
        break
if s==0:
    print('YES')
else:
    print('NO')
    
