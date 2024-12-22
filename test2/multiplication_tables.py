i = 1

def tables(i):
    for j in range(1 , 10):
        print( f"{i} * {j}  = {i * j}")

for i in range(1 , 10):
    tables(i)
    print("-------------------------")