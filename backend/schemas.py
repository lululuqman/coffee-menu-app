from pydantic import BaseModel

class CoffeeBase(BaseModel):
    name: str
    description: str
    price: float

class CoffeeCreate(CoffeeBase):
    pass

class Coffee(CoffeeBase):
    id: int

    class Config:
        from_attributes = True