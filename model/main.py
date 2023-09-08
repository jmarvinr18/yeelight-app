from sqlalchemy.orm import sessionmaker
from model.connect import engine

Session = sessionmaker(bind=engine)

session = Session()
