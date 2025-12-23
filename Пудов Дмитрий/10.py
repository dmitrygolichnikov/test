f=input()
if 'f' in f:
    print(f.find('f'))
    f=f.replace('f','0',1)
    f=f[-1::-1]
if 'f' in f:
    print(len(f)-f.find('f')-1)
