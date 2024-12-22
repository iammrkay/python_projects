val = int(input("enter the number "))

def reverse_number(val):
    reverse_number = 0
    while val > 0:
        reminder = val % 10
        reverse_number = (reverse_number * 10) + reminder
        val = val // 10
    return reverse_number

print("the reverse number of ",val , "is ",reverse_number(val))

if (val == reverse_number(val)):
    print("The number is palindrome")
else:
    print("The number is not palindrome")