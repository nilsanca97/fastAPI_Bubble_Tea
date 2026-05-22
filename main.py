from fastapi import FastAPI
from typing import TypedDict

app = FastAPI()

class BubbleTea(TypeDict):
    id: int
    name: str
    temperature: float
    price: float
    active: bool

bubbleTeas: list[BubbleTea] = [
    {"id": 1, "name": "Classic Milk Tea", "temperature": 5.0, "price": 3.50, "active": True},
    {"id": 2, "name": "Taro Bubble Tea", "temperature": 4.0, "price": 4.00, "active": True}, 
    {"id": 3, "name": "Green Tea Bubble Tea", "temperature": 3.0, "price": 3.75, "active": True},
    {"id": 4, "name": "Black Tea Bubble Tea", "temperature": 2.0, "price": 3.25, "active": False},
]

@app.get("/")
def read_root():
    return {"message": "Hola FastAPI"}

# 🔹 GET hardcodeado de Bubble Tea
@app.get("/bubble-tea")
def get_bubble_tea():
    return bubbleTeas

# filter inactive bubble teas
def filter_inactive_bubble_teas() -> list[BubbleTea]:
    return [tea for tea in bubbleTeas if tea["active"]]