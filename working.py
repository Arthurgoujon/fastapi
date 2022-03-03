from ast import For
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
def home():
    return {"data":"Test"}

@app.get("/about")
def about():
    return {"data":"about"}

inventory = {
    10 : {
        "name": "milk"
    }
}

@app.get("/item/{item_id}")
def getitem(item_id: int = Path(None, description="some description", gt=2)):
    return inventory[item_id]

@app.get("/item_by_name")
def getItemByName(name: str):
    for i in inventory:
        if inventory[i]["name"] == name:
            return inventory[i]
    return "nope"