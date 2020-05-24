"""Install all pkgs """
from web_database.configdatabse import Create_WithSJ_Database
import os
os.system("pip install flask_wtf")
os.system("pip install bs4")
Create_WithSJ_Database()


