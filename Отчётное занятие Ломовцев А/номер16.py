A=list(map(int,input().split()))
z=max(A)+1
mini=z
for x in A:
    if x<mini and x%2==1:
        mini=x
if mini==z:
    print('0')
else:
    print(mini)
    
