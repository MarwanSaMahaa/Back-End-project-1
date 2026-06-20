from fastapi import FastAPI
from productsFastapiHandeler import app as products_app
from authFastapiHandeler import app as auth_app

app = FastAPI()

app.mount("/products-api", products_app)
app.mount("/auth-api", auth_app)