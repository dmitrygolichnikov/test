a=int(input())
b=int(input())
c=int(input())
if a+b>c:
    if c+a>b:
        if b+c>a:
            print('yes')
        else:
            print('no')        
    else:
        print('no')
        
else:
    print('no')