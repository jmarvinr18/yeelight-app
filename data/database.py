import sqlite3
from yeelight import discover_bulbs
from migrations.main import *


def connection():
    conn = sqlite3.connect('data/data.db')

    # CREATE TABLE
    tables = Migration.tables

    for i in range(len(tables)):
        table_create_query = f'''CREATE TABLE IF NOT EXISTS {tables[i].name}
                                {tables[i].db_columns}'''
        conn.execute(table_create_query)

    conn.close()


def discover():
    bulbs = discover_bulbs()
    print(bulbs)


# discover()
connection()
