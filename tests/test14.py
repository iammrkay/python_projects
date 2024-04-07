num = int(input("enter the number"))

def sum1(num):
    sum = 0
    for i in range(1,num):
        sum = sum +i
    return sum


print("sum of number is ",sum1(num))
