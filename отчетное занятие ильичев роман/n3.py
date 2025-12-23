a = int(input())
b = int(input())
n = int(input())
a = a*n
b = b*n
while b > 100:
    a+=1
    b = b-100
print(a, b)