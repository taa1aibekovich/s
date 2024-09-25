from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product
from schema import ProductListValidate

app = FastAPI(title='product')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/create/', response_model=ProductListValidate)
def create_product(car: ProductListValidate, db: Session = Depends(get_db)):
    db_car = Product(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


@app.post('/create/', response_model=ProductListValidate)
def create_car(car: ProductListValidate, db: Session = Depends(get_db)):
    db_car = Product(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


@app.get('/cars/', response_model=list[ProductListValidate])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cars = db.query(Product).offset(skip).limit(limit).all()
    return cars


@app.get('/cars/{car_id}', response_model=ProductListValidate)
def read_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(Product).filter(Product.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail='Car not found')
    else:
        return car


@app.put('/cars/update/{car_id}', response_model=ProductListValidate)
def update_car(car_id: int, car: ProductListValidate, db: Session = Depends(get_db)):
    db_car = db.query(Product).filter(Product.id == car_id).first()

    if db_car is None:
        raise HTTPException(status_code=404, detail='Car not found')

    for key, value in car.dict().items():
        setattr(db_car, key, value)

    db.commit()
    db.refresh(db_car)
    return db_car


@app.delete('/cars/delete/{car_id}', response_model=ProductListValidate)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(Product).filter(Product.id == car_id).first()

    if db_car is None:
        raise HTTPException(status_code=404, detail='Car not found')

    db.delete(db_car)
    db.commit()
    return db_car