import sqlite3,os

DATABASE_PATH=os.environ["Database"]
DATABASE_FILE = "WithSJ_Database//database.db"

def connect_database():
    """Connect to Database and return connetion object"""
    os.chdir(DATABASE_PATH)
    conn=sqlite3.connect(DATABASE_FILE)
    return conn