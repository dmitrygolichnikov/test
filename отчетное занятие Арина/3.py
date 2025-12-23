input_list = ['A a 14 75',
              'B b 23 74',
              'A a 14 75',
              'C c 23 74',
              'B b 23 74']

tmp_list = []
for i in range(len(input_list)):
    tmp_list+=[[input_list[i].split()[3]] + input_list[i].split()[:2]]
    
for i in range(len(tmp_list)):
    for j in range(len(tmp_list)-i-1):        
        for h in range(3):
            for m in range(min(len(tmp_list[j][h]), len(tmp_list[j+1][h]))):
                if ord(tmp_list[j][h][m])>ord(tmp_list[j+1][h][m]):
                    tmp_list[j], tmp_list[j+1] = tmp_list[j+1], tmp_list[j]
                    input_list[j], input_list[j+1] = input_list[j+1], input_list[j]


print(input_list)