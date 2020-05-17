from web_database import connect_database

class BlogPost():
    def __init__(self,title,date,post):
        self.title = title 
        self.date = date
        self.post = post    

    def upload(self):
        conn = connect_database()
        conn.execute("""
        INSERT INTO Blogs(Title,Date,Post)
        VALUES(:title,:date,:post)
        """,{"title":self.title,"date":self.date,"post":self.post})
        conn.commit()
        conn.close()

class Portfolio(BlogPost):
    def upload(self):
        conn = connect_database()
        conn.execute("""
        INSERT INTO Portfolio(Title,Date,Post)
        VALUES(:title,:date,:post)
        """,{"title":self.title,"date":self.date,"post":self.post})
        conn.commit()
        conn.close()