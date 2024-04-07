n = int(input("enter number of values"))
list = []
for i in range(n):
    num = int(input())
    list.append(num)
    
ind1 = int(input("enter index 1 "))
ind2 = int(input("enter index 2 "))

print(list)
temp = list[ind1]
list[ind1]=list[ind2]
list[ind2]= temp
print(list)