a = int(input())
if a < 1000:
    b = a//10-10
elif a < 10000:
    b = a//100-10
print(b)