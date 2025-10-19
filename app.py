from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os

from typing import Optional
# from model import Product

load_dotenv()

app = FastAPI(title="Simple FastAPI App", version="1.0.0")

data = [{"name": "Sam Larry", "age": 20, "track": "AI Developer"},
    {"name": "Bahubali", "age": 21, "track": "Backend Developer"},
    {"name": "John Doe", "age": 22, "track": "Frontend Developer"}]

class Item(BaseModel):
    name: str = Field(..., example="Perpetual")
    age: int = Field(..., example=25)
    track: str = Field(..., example="Fullstack Developer")

# products = [
#     Product(id=1, name="Laptop", price=99.99, quantity=10),
#     Product(id=2, name="Gaming Laptop", price=999.99, quantity=8),
#     Product(id=3, name="Iphone", price=399.99, quantity=100)
# ]

@app.get("/")
def root():
    return {"Message": "Welcome to my FastAPI Application"}


@app.get("/get-data")
def get_data():
    return data


@app.post("/create-data")
def create_data(req: Item):
    data.append(req.dict())
    return {"Message": "Data Received", "Data": data}


@app.put("/update-data/{id}")
def update_data(id: int, req: Item):
    data[id] = req.dict()
    print(data)
    return {"Message": "Data Updated", "Data": data}



# @app.get("/products")
# def get_all_product():
#     return products


# @app.get("/product/{id}")
# def get_product_by_id(id: int):
#     for product in products:
#         if product.id == id:
#             return product
        
#     return "product not found!"


# @app.post("/product")
# def add_product(product: Product):
#     products.append(product)
#     return product


# @app.put("/product")
# def update_product(id: int, product: Product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return "Product added successfully!"
        
#     return "Product not found!"


# @app.delete("/product")
# def delete_product(id: int):
#     for i in range(len(products)):
#         if products[i].id == id:
#             del products[i]
#             return "Product deleted!"
        
#     return "Product not found!"


@app.delete("/product")
def delete_product(id: int):
    for i in range(len(data)):
        if i == id - 1:
            # print(f"Data with name {data[i]['name']} is about to be deleted!")
            del data[i]
            return "Data deleted successfully"
    
        return "Data not found!!!"
    
    
@app.patch("/product/{id}")

def edit_product(id: int, name: Optional[str] = None, age: Optional[int] = None, track: Optional[str] = None):
    for i in range(len(data)):
        if i == id -1:
            if name is not None:
                data[i]["name"] = name
            if age is not None:
                data[i]["age"] = age
            if track is not None:
                data[i]["track"] = track
            return f"Data updated successfully. {data[i]}"
    return "Data not found!"
    
    


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
