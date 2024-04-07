def number_reverse(num):
    nn = 0
    while (num >0):
        r = num %10
        nn = (nn *10)+ r
        num = num //10
    return nn

num = int(input("enter the number"))
print("the revers of the number is ",number_reverse(num))

