a=int(input())
b=int(input())
c=int(input())
s=0
if a+b>c:
    s+=1
if a+c>b:
    s+=1
if c+b>a:
    s+=1
if s==3:
    print('YES')
else:
    print('NO')
          
