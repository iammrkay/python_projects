arr = [10,20,30,40]
n = int(input("Enter the  n walue"))

def sum_array(arr,n):
    sum = 0
    for i in arr:
        sum = sum + i
    i = i%n
    return i
print("The sum of array is ",sum(arr,n))