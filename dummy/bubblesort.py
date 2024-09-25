array = [1, 2, 5, 3, 7, 6, 5]
print(array)
def sort(array):
    for i in range(len(array)):
        # Find the minimum element in the unsorted subarray
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]
sort(array)
print(array)
        