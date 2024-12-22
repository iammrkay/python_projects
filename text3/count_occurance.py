sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

def count_orrucance(sample_list):
    cont_dict = dict()
    for item in sample_list:
        if item in cont_dict:
            cont_dict[item] +=1
        else:
            cont_dict[item] = 1
    print("the item count is " ,cont_dict)
count_orrucance(sample_list)

