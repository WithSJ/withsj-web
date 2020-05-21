from web_database import connect_database

class Get_Blogs():
    def data(self):
        """Get all data from blogs table"""
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Blogs ORDER BY Date DESC")
        return cur.fetchall()

class Get_Portfolio():
    def data(self):
        """Get all data from portfolio table"""
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Portfolio")
        return cur.fetchall()

