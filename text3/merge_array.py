l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

newLi = []
for i in range(1 , len( l1), 2):
    newLi.append(l1[i])

for i in range(0 , len( l2), 2):
    newLi.append(l2[i])


print("the new list is ", newLi)    