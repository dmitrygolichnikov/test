my_list = list(map(int,input().split()))
count = 1
for i in range(len(my_list)):
    i += 1
    while my_list[i] > my_list[i+1] and my_list[i] > my_list[i-1]:
        count += 1
print(count-1)