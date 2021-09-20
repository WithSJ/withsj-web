import sqlite3,os


DATABASE_PATH=os.getcwd()



DATABASE_FILE = "WithSJ_Database//database.db"
DATABASE_IMAGES = os.path.join(DATABASE_PATH,"WithSJ_Database/Files/Images/") 
def connect_database():
    """Connect to Database and return connetion object"""
    os.chdir(DATABASE_PATH)
    conn=sqlite3.connect(DATABASE_FILE)
    return conn
