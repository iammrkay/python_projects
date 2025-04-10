from fastapi import FastAPI

app = FastAPI()

items = []

@app.get('/')
def root():
    return {'hello': 'world'}

@app.post("/item/")
def create_item(name:str, price:float):
    return{"name":name,"price":price}

@app.put('/item/{item_id}')
def update_item(item_id: int,name:str, price:float ):
    return {"item_id":item_id, "name":name, "price":price}

@app.delete('/item/{item_id}')
def delete_item(item_id: int,):
    return{"messge": f"item {item_id} deketed successfuly "}