str = input("enter the input string ")

def even_char(str):
    for i in range(len(str)):
        if (i % 2 == 0):
            print(str[i])
        

even_char(str)