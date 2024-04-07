# #factorial of integer.
# n = int(input("enter number"))

# def factorial1(n):
#     ans = 1
#     if n == 0:
#         ans = 1
#     else:
#         for i in range(1,n+1):
#             ans = i * ans
    
#     return ans    

# output =  factorial1(n)
# print("the output is ", output)


# factorial function.
# n = int(input("enter a number "))

# def factorial(n):
#     ans = 1
#     if n == 0:
#         ans = 1
#     else:
#         for i in range(1, n+1):
#             ans = ans *i
#     return ans

# output = factorial(n)
# print("The factorial of ",n, "is ",output)

def fact(n):
    #base codition
    if n == 0:
        return 1
    
    #recursive case
    ans = n * fact(n-1)
    return ans
print(fact(6))


        