from fastapi import FastAPI
from typing import TypedDict

app = FastAPI()

class BubbleTea(TypedDict):
    id: int
    name: str
    temperature: float
    price: float
    active: bool

class tapa(TypedDict):
    id: int
    name: str
    price: float
    active: bool

bubbleTeas: list[BubbleTea] = [
    {"id": 1, "name": "Classic Milk Tea", "temperature": 5.0, "price": 3.50, "active": True},
    {"id": 2, "name": "Taro Bubble Tea", "temperature": 4.0, "price": 4.00, "active": True}, 
    {"id": 3, "name": "Green Tea Bubble Tea", "temperature": 3.0, "price": 3.75, "active": True},
    {"id": 4, "name": "Black Tea Bubble Tea", "temperature": 2.0, "price": 3.25, "active": False},
]

tapas: list[tapa] = [
    {"id": 1, "name": "Patatas Fritas", "price": 2.50, "active": True},
    {"id": 2, "name": "Albondigas", "price": 3.00, "active": True},
    {"id": 3, "name": "Croquetas", "price": 2.75, "active": False},
    {"id": 4, "name": "Ensalada César", "price": 4.50, "active": True},
    {"id": 5, "name": "Quesadillas", "price": 3.25, "active": True},
]

@app.get("/")
def read_root():
    return {"message": "Hola FastAPI"}

# 🔹 GET hardcodeado de Bubble Tea
@app.get("/bubble-tea")
def get_bubble_tea():
    return filter_inactive_bubble_teas()
# GET harcodeade de Tapas
@app.get("/tapas")
def get_tapas():
    return filter_inactive_tapas()

# filter inactive bubble teas
def filter_inactive_bubble_teas() -> list[BubbleTea]:
    return [tea for tea in bubbleTeas if tea["active"]]

# filter inactive tapas
def filter_inactive_tapas() -> list[tapa]:
    return [tapa for tapa in tapas if tapa["active"]]