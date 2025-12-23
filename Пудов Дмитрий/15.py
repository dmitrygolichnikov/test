def isprime(x):
    respect=True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            respect=False
            break
    return respect
if isprime(int(input()))==True:
    print('YES')
else:
    print("NO")