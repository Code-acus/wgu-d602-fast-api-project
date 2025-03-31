import json
from pydantic import BaseModel

class CarInput(BaseModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"

class CarOutput(BaseModel):
    id: int

    @classmethod
    def from_input(cls, car_input: CarInput, price_per_hour: float) -> "CarOutput":
        return cls(**car_input.model_dump(), price_per_hour=price_per_hour)

def load_db() -> list[CarOutput]:
    """Load the database from a JSON file."""
    with open("cars.json") as f:
        return [CarInput.model_validate(obj) for obj in json.load(f)]

def save_db(cars: list[CarOutput]):
    with open("cars.json", "w") as f:
        json.dump([car.model_dump() for car in cars], f, indent=4)
