str = input("enter the string ")
n = int(input("enter the number"))
def remove_char(str, n):
    return str[n:]

print("the extracted string is ",remove_char(str, n))
