import json
from pydantic import BaseModel

# The effect of this is a like jangled models
class Car(BaseModel):
    id: int
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"

def load_db() -> list[Car]:
    """ Load the database from a JSON file """
    with open("cars.json") as f:
        # This simulates a database
        return [Car.model_validate(obj) for obj in json.load(f)]