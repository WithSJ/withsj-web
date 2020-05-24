"""
    This py use to create databse.db file in WithSJ_Database for website and tables in it
    Note:- WithSJ_Database folder contain *.db files for server backup file also created here
            name of backup *.db file are in format (Date-and-time.databse.db)
    
    |WARRING| 
        be carefull when use run this py file because it may be remove all databse.db 
        file data if it already exits use it when you backup your databse.db files 
"""
from web_database import os,sqlite3,DATABASE_PATH,connect_database

class Create_WithSJ_Database():

    def __init__(self):
        self.connect_database()
    
    def connect_database(self):
        """ Connect to Database or Create database folders and file if file not exist
        """
        if os.path.exists(os.path.join(DATABASE_PATH,"WithSJ_Database")):
            conn = connect_database()            
            self.config_database(conn)
        else:
            os.mkdir(os.path.join(DATABASE_PATH,"WithSJ_Database"))
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
                Post TEXT NOT NULL,
                BlogID TEXT NOT NULL UNIQUE
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
