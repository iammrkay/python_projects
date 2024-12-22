def exponent(num, exp):
    result = 1
    while (exp> 0):
        result = result * num
        exp = exp - 1
    return result
print("the exponent of 5 raise 2 is ",exponent(5 , 5))