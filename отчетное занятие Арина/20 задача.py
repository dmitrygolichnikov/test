num = int(input())
my_list = [[0] * num for i in range(num)]

for i in range(num):
    for j in range(num):
        if i == j:
            my_list[][] = 1

for i in my_list:
    print(' '.join(map(str, i)))
print()