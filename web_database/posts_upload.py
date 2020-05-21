from web_database import connect_database
from random import randint
class BlogPost():
    def __init__(self,title,date,post):
        self.title = title 
        self.date = date
        self.post = post    

    def upload(self):
        conn = connect_database()
        conn.execute("""
        INSERT INTO Blogs(Title,Date,Post,BlogID)
        VALUES(:title,:date,:post,:blogid)
        """,{"title":self.title,"date":self.date,"post":self.post,"blogid":self.get_blogid()})
        conn.commit()
        conn.close()

    def get_blogid(self,h_link = hex(randint(0,32))[2:] ):
        blogid = self.title.replace(" ","%") +"%"+h_link
        return blogid


class Portfolio(BlogPost):
    def upload(self):
        conn = connect_database()
        conn.execute("""
        INSERT INTO Portfolio(Title,Date,Post)
        VALUES(:title,:date,:post)
        """,{"title":self.title,"date":self.date,"post":self.post})
        conn.commit()
        conn.close()