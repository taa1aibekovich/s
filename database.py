from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from schema import ProductListValidate

DB_URL = 'postgresql://postgres:adminadmin@localhost/pythonn5'

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()



