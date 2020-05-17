"""Install all pkgs """
from web_database.configdatabse import Create_WithSJ_Database
import os
os.system("pip install bcrypt")

Create_WithSJ_Database()


