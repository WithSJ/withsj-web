"""
    This py use to create databse.db file in WithSJ_Database for website and tables in it
    Note:- WithSJ_Database folder contain *.db files for server backup file also created here
            name of backup *.db file are in format (Date-and-time.databse.db)
    
    |WARRING| 
        be carefull when use run this py file because it may be remove all databse.db 
        file data if it already exits use it when you backup your databse.db files 
"""
import sqlite3,os

class Create_WithSJ_Database():

    def __init__(self):
        self.database_path = os.environ["Database"]
        self.connect_database()
    
    def connect_database(self):
        """ Connect to Database or Create database folder and file if file not exist
        """
        os.chdir(self.database_path)
        if os.path.exists("WithSJ_Database"):
            conn = sqlite3.connect("WithSJ_Database//database.db")
            self.config_database(conn)
        else:
            os.mkdir("WithSJ_Database")
            self.connect_database()
            print("Database successfully created")

    def config_database(self,conn):
        """ Create Blogs Table and its requred fileds
        """
        try:   
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE Blogs(
                Title TEXT NOT NULL,
                Date TEXT NOT NULL ,
                Post TEXT NOT NULL
                )""")
            
            cur.execute("""
                CREATE TABLE Portfolio(
                Title TEXT NOT NULL,
                Date TEXT NOT NULL ,
                Post TEXT NOT NULL
                )""")
            conn.close()

        except  sqlite3.OperationalError :
            print("Database already exits")