word1= input("enter the word 1 ")
word2= input("enter the word 2 ")

def merge(word1,word2):
    result = []
    leng = len(word1)
    for i in range(leng):
        result.append(word1[i])
        result.append(word2[i])
    return result

print(merge(word1,word2))