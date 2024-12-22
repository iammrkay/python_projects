from icecream import ic
value = input("enter the value  ")
step = 5

for i in range(0, len(value)):
    key = ord(value[i])
    if key == 32:
        value = value.replace(value[i], " ")    
    else:
        value = value.replace(value[i], chr(key+step))
ic(value)



