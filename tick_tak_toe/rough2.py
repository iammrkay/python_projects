import random
from icecream import ic
def function():
    array = []
    c = 0

    for i in range(5):
        c = c+1
        array.insert(i,c)
    #ic(array)
    def shuffle(array):
        ic(array)    
        random.shuffle(array)
        ic(array)
    shuffle(array)
#function()

class student:
    student = {
            'name':'',
            'age':0,
            'gender':''
        }
    def __init__(self,name,age,gender):
        self.student['name']= name
        self.student['age']= age
        self.student['gender']= gender

RAM = student(
    "RAM",
    20,
    'M')
print(RAM.student['age'])