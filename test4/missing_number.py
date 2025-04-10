from icecream import ic

values = [1,2,3,5]
n = len(values)
x1 = 0 
x2 =  0
for i in range(0,n):
    x1 = x1 ^ values[i]
for j in range(0,n+2):
    x2 = x2 ^ j
ic(x1 ^ x2)
