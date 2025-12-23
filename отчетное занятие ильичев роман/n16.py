a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i]%2 != 0 and a[i] > a[i+1]:
        count += 1
print(count)