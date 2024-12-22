data = input("enter the values ")
arra = data.split()

def divisible(arra):
    for i in range(len(arra)):
        if int(arra[i]) % 5 == 0:
            print("The values are ", arra[i])
        
divisible(arra)