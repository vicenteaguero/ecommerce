# api/main.py

from fastapi import FastAPI

from api.endpoints import cart

app = FastAPI()
app.include_router(cart.router, prefix='/api/cart')
