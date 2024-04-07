print("Swap number ")
ar = [10,20,30,40,40]
def swap(ar):
    ar[0] = ar[0]+ar[-1]
    ar[-1] = ar[0]-ar[-1]
    ar[0] = ar[0]-ar[-1]
    return ar
print("The array is ",ar)
print("the swapped array is ",swap(ar))

