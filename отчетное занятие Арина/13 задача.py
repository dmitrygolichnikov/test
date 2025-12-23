number = int(input())
maxi = number
while number != 0:
    number = int(input())
    if number > maxi:
        maxi = number
    
print(maxi)