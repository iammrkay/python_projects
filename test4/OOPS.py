import csv

class Item:
    pay_rate =0.20 
    all = []
    def __init__(self, name:str, price:float,quantity = 0):
        #valud validation
        assert price>=0 , f"price {price} is not greater than 0"
        assert quantity>=0 , f"quantity  {quantity} is not greater than 0"
        
        #valud declaration
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #add values into thhe all list
        Item.all.append(self)
        pass

    def calculate_price(self):
        return self.price*self.quantity
    def apply_discount(self):
        return self.price -(self.price*self.pay_rate)
    @classmethod
    def instantiate_from_csv(cls):
        with open("C:/Users/SkyromaX/Documents/GitHub/python_projects/test4/Abcd.csv",'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
            )
            
            
    def __repr__(self):
        return f"item({self.name},{self.price},{self.quantity})"
    

    
Item.instantiate_from_csv()
print(Item.all)


