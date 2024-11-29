import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)




@app.get("/store") #  endpoint
def get_stores(): #function
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex #random 16 digit number
    new_store ={**store_data, "id": store_id}
    stores[store_id]=new_store
    return  new_store,  201

@app.post("/item")
def create_item(name):
    item_data  = request.get_json()
    if item_data["store-id"] not in stores:
        return {"message": "Store not found"},404
    
    item_id = uuid.uuid4().hex
    item = {**item_data,"id":item_id}
    items[item_id] = item
    return item, 201

#get to a specific store out of many
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return  stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:        
        return  items[item_id]
    except KeyError:
        return {"message": "Store not found"}, 404

