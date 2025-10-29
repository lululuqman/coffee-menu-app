from sqlalchemy.orm import Session
from . import models, schemas

def get_coffees(db: Session):
    return db.query(models.Coffee).all()

def get_coffee(db: Session, coffee_id: int):
    return db.query(models.Coffee).filter(models.Coffee.id == coffee_id).first()

def create_coffee(db: Session, coffee: schemas.CoffeeCreate):
    db_coffee = models.Coffee(**coffee.dict())
    db.add(db_coffee)
    db.commit()
    db.refresh(db_coffee)
    return db_coffee