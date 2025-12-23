b=str(input())
s=0
flag=0
count=0
for i in b:
    count+=1
    if i=='f':
        s+=1
        if flag==0:
            print(count)
            flag=1
if s>1:
    m=len(b)
    b1=b[::-1]
    for j in range(m):
        if b1[j]=='f':
            print(m-j)
            break
