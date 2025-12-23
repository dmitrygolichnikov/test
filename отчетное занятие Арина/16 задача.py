lis = list(map(int, input().split()))
mini = max(lis)

for i in lis:
    if i % 2 != 0 and i < mini:
        mini = i
        
if mini % 2 == 0:
    print(0)
else:
    print(mini)