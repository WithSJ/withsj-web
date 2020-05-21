"""Install all pkgs """
from web_database.configdatabse import Create_WithSJ_Database
import os
os.system("pip install bcrypt")
os.system("pip install flask_wtf")
Create_WithSJ_Database()


