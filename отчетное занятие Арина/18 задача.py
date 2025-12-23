my_list = list(map(int, input().split()))

def IsAscending(A):
    flag = True
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i+1]:
            flag = False
    return flag

g = IsAscending(my_list)
    
if g == True:
    print('YES')
else:
    print('NO')