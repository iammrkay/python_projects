roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

def key_check(roll_number , sample_dict):
    for item in roll_number:
        if item not in sample_dict.values():
            sample_dict.pop(item)
key_check(roll_number , sample_dict)

#unsolved
            