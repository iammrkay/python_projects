fruits = ["Apple","Mango","Cherry","Banana"]
# print(fruits) #print list items
# print(type(fruits))# print type of list ovariable
# print(len(fruits)) # print length of list variable
# if "Banana" in fruits: # check
#     print("Banana presnt in fruits")
# if "chivi" not in fruits:
#     print("kivi is not part of list")

#indexing in List
# print(fruits[1])
# print(fruits[-1])
# print(fruits[1:3]) # gives a sub list of a list
# print(fruits[-3-1])# gives a sub list of a list

# adding elements to a list
# fruits.append("kiwi")
# print(fruits)

#insert values in a list
# fruits.insert(2,"Kiwi")
# print(fruits)

# attaching a list to another list.
# more_fruites = ["Kiwi", "Papaya"]
# fruits.extend(more_fruites)
# print(fruits)


#removing items in a list using remove function
# fruits.remove("Banana")
# print(fruits)

#removeing items using pop functions
# print(fruits)
# fruits.pop(2)
# print(fruits)

#changing values in a list.
# print(fruits)
# fruits[1] = "Kiwi"
# print(fruits)

#change values in a range of items in a list
# print(fruits)
# fruits[1:3] = ["Papaya"]
# print(fruits)

#sorting in list
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)
# fruits.reverse()
# print(fruits)

# create a new sublist with a condition by collecting items from an existing list
# new_list = [i for i in fruits if "a" in i]
# print(new_list)

#Copy a fruits list
# new_list = fruits.copy()
# print(new_list)

# #To concatinate two lists.
# print(new_list + fruits)