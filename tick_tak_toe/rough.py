import random
from icecream import ic
count = 1
array = []

for i in range(5):
    array.insert(i , count)
    count = count +1
ic(array)
k = 0
ran_array = {}
for k in array:
    k = k + 1
    ran_val = random.choice(array)
    if ran_val in ran_array:
        print(ran_val," already exists")
    else:
        ran_array[ran_val]=k
ic(ran_array.keys())


