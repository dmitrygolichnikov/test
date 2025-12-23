def func(A):
    for i in range(len(A)-1):
        if A[i] >= A[i+1]:
            return False
    return True

list1 = list(map(int, input().split()))

if func(list1):
    print('yes')
else:
    print('no')