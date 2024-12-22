#subset of a string confirmation program.

string1 = input("enter the 1st string ")
string2 = input("enter the 2nd string ")

def subset_string(string1 , string2):
    i , j = 0 , 0
    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            i = i + 1
        j = j + 1
    result = i == len(string1)
    return result

print(subset_string(string1 , string2))
    
