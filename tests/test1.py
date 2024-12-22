import math

arr = []
arr2 = [10,20,23,24,44,21,23,23,55,64,12,85,65,79,15,97,65,55]

#[10,20,23,24]
#[44,21,23,23]
#[55,64,12,85]
#[65,79,15,97]
#[65,55,0,0]
def dimensions(arr):
    length =len(arr2)
    row = math.sqrt(length)
    return int(row)
col = dimensions(arr2)

def array2d(arr):
    r = col
    arr3 = []
    for i in range(len(arr)):
        new_row = []
        c = 0
        for j in range(i, r+i):   
            if j< len(arr):
                new_row.insert(c,arr[j])
                c = c + 1
        arr3.append(new_row)
        i = i+ r
        
    print(arr3)
array2d(arr2)

count = 0

# for i in range(row):
#     new_row = []
#     for j in range(col):
#         count = count +1
#         new_row.insert(j,arr2[j])
#     arr.append(new_row)
#     print("\n")


# def display_array(arr):
#     for i in range(row):
#         for j in range(col):
#             print(arr[i][j], end = "\t")
#         print("\n")

# display_array(arr)