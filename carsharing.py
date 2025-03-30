import uvicorn
from fastapi import FastAPI
from schemas import load_db
from schemas import Car
from fastapi import HTTPException
from schemas import save_db

app = FastAPI()

db = load_db()

@app.get("/api/cars")
def get_cars(size: str|None = None, doors: int|None = None) -> list:
    result = db
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors >= doors]
    return result

# Path parameter
@app.get("/api/cars/{id}")
def get_car_by_id(id):
    result = [car for car in db if car["id"] == id]
    if not result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail="Not found")

@app.post("/api/cars")
def add_car(car: Car):
    db.append(car)
    save_db(db)

if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)