# api/main.py

from fastapi import FastAPI

from api.src.endpoints import router

app = FastAPI()
app.include_router(router, prefix='/api/cart')
