import uvicorn
from fastapi import FastAPI, HTTPException
from schemas import load_db, CarInput, save_db, CarOutput

app = FastAPI()

db = load_db()

@app.get("/api/cars")
def get_cars(size: str | None = None, doors: int | None = None) -> list[CarInput]:
    result = db
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors >= doors]
    return result

@app.get("/api/cars/{id}")
def get_car_by_id(id: int) -> CarInput:
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail="Not found")

@app.post("/api/cars")
def add_car(car: CarInput) -> CarOutput:
    new_car = CarInput(
        size=car.size,
        doors=car.doors,
        fuel=car.fuel,
        transmission=car.transmission
    )
    new_id = len(db) + 1  # Removed the extra parenthesis

if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)
