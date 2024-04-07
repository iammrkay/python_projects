list = [23,65,19,90]


ind1 = int(input("enter 1st indes number"))
ind2 = int(input("enter 2nd index number"))
print(list)
temp = list[ind1]
list[ind1] = list[ind2]
list[ind2] = temp

print(list)