from web_database import connect_database

class Get_Blogs():
    def data(self):
        """Get all data from blogs table"""
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Blogs ORDER BY Date DESC")
        data_dic_list = list()
        data_dict = dict()
        data_list = cur.fetchall()
        for data in data_list:
            data_dict["title"] = data[0]
            data_dict["date"] = data[1]
            data_dict["post"] = data[2]
            data_dict["blogid"] = data[3]
            data_dic_list.append(data_dict)
            data_dict = dict()
        del data_dict,data_list
        return data_dic_list


class Get_Blogpage():
    """GEt data from blod id only one row get"""
    def __init__(self,Blog_ID):
        self.Blog_ID = Blog_ID
    def data(self):
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Blogs WHERE BlogID = :blogid""",{"blogid":self.Blog_ID})
        return cur.fetchone()

class Get_Portfolio():
    def data(self):
        """Get all data from portfolio table"""
        conn = connect_database()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Portfolio")
        return cur.fetchall()

