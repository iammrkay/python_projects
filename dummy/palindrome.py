
str = input("enter the string ")

def palindrom(str):
    print(str[::-1])
    if str == str[::-1]:
        return True
    else:
        return False
    
print("the palindrome string is ",palindrom(str))
