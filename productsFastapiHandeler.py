import productsCrud
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/product")
def create_product(name: str, price: int, quantity: int):
    productsCrud.create(name, price, quantity)
    return {"message": "Product created successfully"}

@app.get("/products")
def read_all_products():
    return productsCrud.get_all()

@app.get("/product")
def read_one_product(name: str):
    return productsCrud.get(name)

@app.put("/product")
def update_product(old_name: str, new_name: str, price: int, quantity: int):
    productsCrud.update(old_name, new_name, price, quantity)
    return {"message": "Product updated successfully"}

@app.delete("/product")
def delete_product(name: str):
    productsCrud.delete(name)
    return {"message": "Product deleted successfully"}
