list1 = [54, 44, 27, 79, 91, 41]

def modified_array(list1):
    del_item = list1.pop(4)
    print("the array after deletion is ",list1)
    add_item = list1.insert(2,del_item)
    print("the array after addition ",list1)

print("the array = ",list1)
modified_array(list1)