number = int(input("enter the number "))

if number == 0:
    number = 1
    
def current_sum(number):
    previous_number = 0
    for i in range(number):
        print("current number is ", i + previous_number)
        print("previous number is ", i)
        previous_number = i

current_sum(number)