import math
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

def convert_array(arr , col):
    # print(arr)
    # print(col)
    result = []
    c = 0
    for i in range(col):
        new_row = []
        for j in range(col):
            new_row.insert(j,arr[c])
            c = c + 1
        result.append(new_row)
    # print(result)
    return result
result_array = convert_array(arr2, col)

def print_array(result_array , col):
    # print(result_array)
    # print(col)
    for i in range(col):
        for j in range(col):
            print(result_array[i][j], end = "\t")
        print("\n")
print_array(result_array , col)