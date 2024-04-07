n = int(input("Enter numeric value "))
for i in range(1,n+1):
    print(" "* (n - 1) , end="")
    for j in range (1,2 * i):
        print(j, end="")
    print()

