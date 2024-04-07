n1 = int(input("enter the number"))
rnum = 0

while (n1 > 0):
    r = n1%10
    rnum = (rnum*10)+r
    n1 = n1//10

print("the revers of ",n1, "is ",rnum)
