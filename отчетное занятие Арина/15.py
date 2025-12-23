a=int(input())
def isPrime(a):
    for i in range(2,int(a**(1/2))+1):
        if a==i:
            return True
        
        if a/i==a//i:
            return False
        
    return True
b=isPrime(a)
if b:
    print('yes')
else:
    print('no')