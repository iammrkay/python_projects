import json
from icecream import ic
def load():
    dict = {
        'name':'abcd',
        'age':10,
        'gender':'M'
    }

    j_string = json.dumps(dict, indent=2)
    with open('myjson.json','w')as f:
        f.write(j_string)
        
#load()

def read():
    with open('myjson.json','r') as f:
        j_object = json.loads(f.read())
        print(j_object['name'])
read()

class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        print(self.name,self.age,self.gender)
    def older(self,years):
        self.age += years
