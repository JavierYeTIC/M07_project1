from fastapi import FastAPI, UploadFile 

from db import clientPS
from db import productDB
from model.Product import Product

from schema import jsonPro
from schema import jsonProAll
from schema import jsonProId


app = FastAPI()

try:
    conn = clientPS.client()
except Exception as e:
        print(f"Error connecting to the database: {e}")

#(1, 'informatica', current_timestamp, current_timestamp);
# uvicorn main:app --reload

@app.get("/")
def hello_world():
    return "Hello, World!"

# Ruta: /products/
@app.get("/products")
def get_all_products():
    # if conn is None:
    #     raise HTTPException(status_code=500, detail="Database connection not established")
    # products =  productDB.consulta()
    data = productDB.consulta()
    datajson = jsonPro.product_schema(data)
    return datajson

# Ruta: /product/{product_id}
@app.get("/product/{product_id}")
def get_product_by_id(product_id:int):
    # if conn is None:
    #     raise HTTPException(status_code=500, detail="Database connection not established")
    data = productDB.consultaiD(product_id)
    datajson = jsonProId.product_schema(data)
    return datajson


@app.post("/product/")
def create_product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at):
    #VALUES (4, 'iphone 15 pro max', '1TB', 'iphone', 1500, 1, 2, current_timestamp, current_timestamp);
    productDB.inserta(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at)
    return {"message": "S'ha afegit correctament"}

# Actualitzar por ID
@app.put("/product/{id}")
def updateProductById(id:int, prod:Product):
    productDB.edit(id,prod)
    return {f"Producte amb el id {id} actualitzat"}

# Delete un product
@app.delete("/product/{id}")
def deleteProductById(id:int,prod:Product):
    productDB.borrar(id)
    return {f"Producte {prod.name} borrat!"}

# Return totas els productes
@app.get("/productAll/")
def allProducts():
    data = productDB.productAll()
    datajson = jsonProAll.product_schema(data)
    return datajson

# suvir productes a la bd desde un CSV
@app.post("/loadProducts")
async def create_upload_file(file: UploadFile):
    csvProducts= productDB.pujarCSV(file)
    return csvProducts