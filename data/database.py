import sqlite3
from yeelight import discover_bulbs
from migrations.main import *
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///mydb.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()




class Person(Base):

    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)
    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

Base.metadata.create_all(bind=engine)

# person = Person
# def connection():
#     conn = sqlite3.connect('data/data.db')
#
#     # CREATE TABLE
#     tables = Migration.tables
#
#     for i in range(len(tables)):
#         table_create_query = f'''CREATE TABLE IF NOT EXISTS {tables[i].name}
#                                 {tables[i].db_columns}'''
#         conn.execute(table_create_query)
#
#     conn.close()
#
#
# def discover():
#     bulbs = discover_bulbs()
#     print(bulbs)
#
#
# # discover()
# connection()
