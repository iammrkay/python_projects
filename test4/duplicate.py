value = [1,2,3,2]
hashset = set()

for i in value:
    if i in hashset:
        print("duplicate value is ",i)
    hashset.add(i)
print("the values is ",value)