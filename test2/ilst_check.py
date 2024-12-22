values = [10, 20, 30, 40, 10]

def number_check(values):
    result = None
    
    if values[0] == values[len(values)]:
        result = True
    else:
        result = False
    return result

print("The number check is ",number_check(values))

