from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app=FastAPI()
@app.get("/")
def root():
    return {"status": "ok"}
class Fruit(BaseModel):
    id:int
    name:str
    quantity:int
    price:float
fruits=[
    Fruit(id=1,name="Apple",quantity=50,price=30),
    Fruit(id=2,name="mango",quantity=50,price=302),
    Fruit(id=3,name="Orange",quantity=50,price=305),
    Fruit(id=4,name="Pineapple",quantity=50,price=300)
]
@app.get("/fruits/{id}")
def get_fruits_by_id(id:int):
    for Fruit in fruits:
        if Fruit.id==id:
            return Fruit
    return "Fruits not found"
@app.get("/fruits")
def get_all_fruits():
    return fruits
@app.post("/fruits")
def post_fruits_by_id(Fruit:Fruit):
       fruits.append(Fruit)
       return {
           "message":"Fruits added succesfully",
           "fruit":Fruit
       }    
@app.put("/fruits/{id}")
def update_fruits(id: int, updated_fruit: Fruit):

    for i in range(len(fruits)):
        if fruits[i].id == id:
            fruits[i].name = updated_fruit.name
            fruits[i].quantity = updated_fruit.quantity
            fruits[i].price = updated_fruit.price

            return {
                "message": "Fruit updated successfully",
                "fruit": fruits[i]
            }

    return {"error": "Fruit not found"}
@app.delete("/fruits/{id}")
def delete_fruits(id:int,Fruit:Fruit):
    for i in range(len(fruits)):
        if fruits[i].id==id:
          deleted_Fruit=fruits.pop(i)
          return {
              "message":"Fruit deleted succesful",
              "Fruits":deleted_Fruit
          }

