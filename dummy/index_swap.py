print("index swap")
ar = [10,20,30,40,50]
n1 = int(input("enter 1st index "))
n2 = int(input("enter 2nd index "))
def ind_swap(ar,n1,n2):
    ar[n1],ar[n2] = ar[n2],ar[n1]
    return ar
print("The array is ",ar)
print("The swaped array is ",ind_swap(ar,n1,n2))
