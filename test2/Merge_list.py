list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def merge_list(list1 , list2):
    newl1 = []
    for i in list1:
        if i % 2 !=0:
            newl1.append(i)
    for j in list2:
        if j % 2 ==0:
            newl1.append(j)
    return newl1


print("The merded lists is ",merge_list(list1 , list2))