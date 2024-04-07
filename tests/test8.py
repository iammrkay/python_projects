input_tup = (1,2,3,4,5)
list = []

print(input_tup)
for x in reversed(input_tup):
    list.append(x)
output_tup = tuple(list)

print(output_tup)