from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/coffees")
def read_coffees(db: Session = Depends(get_db)):
    return crud.get_coffees(db)

@app.post("/coffees")
def create_coffee(coffee: schemas.CoffeeCreate, db: Session = Depends(get_db)):
    return crud.create_coffee(db, coffee)

@app.put("/coffees/{coffee_id}")
def update_coffee(coffee_id: int, coffee: schemas.CoffeeCreate, db: Session = Depends(get_db)):
    db_coffee = crud.update_coffee(db, coffee_id, coffee)
    if db_coffee is None:
        raise HTTPException(status_code=404, detail="Coffee not found")
    return db_coffee

@app.delete("/coffees/{coffee_id}")
def delete_coffee(coffee_id: int, db: Session = Depends(get_db)):
    success = crud.delete_coffee(db, coffee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Coffee not found")
    return {"message": "Deleted successfully"}