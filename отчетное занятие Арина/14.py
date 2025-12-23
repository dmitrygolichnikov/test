x=float(input())
y=float(input())
def isPoint(x,y):
    return abs(x+y)>2
v=isPoint(x,y)
if v:
    print('no')
else:
    print('yes')