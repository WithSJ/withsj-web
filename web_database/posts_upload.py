from web_database import connect_database, DATABASE_IMAGES
from random import randint
from flask import url_for
class BlogPost():
    def __init__(self,title,date,post,image=None):
        self.title = title 
        self.date = date
        self.post = post    
        self.image = image

    def upload(self):
        rand_link = hex(randint(0,32))[2:]
        get_blogid = self.get_blogid(h_link=rand_link)
        
        if self.image != None:
            self.image.save(DATABASE_IMAGES + get_blogid) #backup images
            # self.image.save(url_for('static',filename='images/' + get_blogid))

        conn = connect_database()
        conn.execute("""
        INSERT INTO Blogs(Title,Date,Post,BlogID)
        VALUES(:title,:date,:post,:blogid)
        """,{"title":self.title,"date":self.date,"post":self.post,"blogid":get_blogid})
        conn.commit()
        conn.close()

    def get_blogid(self,h_link = hex(randint(0,32))[2:] ):
        blogid = self.title.replace(" ","+") +"+"+h_link
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Blogs WHERE BlogID = :blogid", {"blogid":blogid})
        data = cur.fetchone()
        if data == None:
            return blogid
        else:
            h_link=hex(randint(0,32*2))[2:]
            self.get_blogid(h_link)

class Portfolio(BlogPost):
    def upload(self):
        conn = connect_database()
        conn.execute("""
        INSERT INTO Portfolio(Title,Date,Post)
        VALUES(:title,:date,:post)
        """,{"title":self.title,"date":self.date,"post":self.post})
        conn.commit()
        conn.close()