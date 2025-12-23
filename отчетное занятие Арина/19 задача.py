n, m = list(map(int, input().split()))
my_list = [list(map(int, input().split())) for i in range(n)]
maxi = my_list[0][0]
ind = ''

for i in range(len(my_list)):
    for j in range(len(my_list)):
        if my_list[i][j] > maxi:
            maxi = my_list[i][j]
            ind = str(i) + ' ' + str(j)
    
print(ind)