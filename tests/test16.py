# print numbers from n to 1
n = int(input("enter the number "))
def number(n):
    if n == 1:
        return 1
    
    print(n)
    number(n-1)
output = number(n)