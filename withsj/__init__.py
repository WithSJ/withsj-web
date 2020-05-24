
from flask import Flask,render_template,url_for,flash,redirect
from web_database.get_posts import Get_Blogs,Get_Portfolio,Get_Blogpage
from web_database.posts_upload import BlogPost
from withsj.form import LoginForm , AdminPannelForm, BlogForm
from random import randint
from datetime import datetime

USERNAME="WithSJ"
PASSWORD="qwerty1234"

app = Flask(__name__)
app.config['SECRET_KEY']="withsj key is here"

def get_adminkey():
    return hex(randint(0,9**64))[2:]

def rendered_to_html(renderhtml):
    """
    Render templates return data str but html reserver char are in code 
    rendered_to_html convert codes to char
    """
    renderhtml= renderhtml.replace('&lt;','<')
    renderhtml = renderhtml.replace('&gt;','>')
    renderhtml = renderhtml.replace('&#34;','"')
    renderhtml = renderhtml.replace('&#39;',"'")
    renderhtml = renderhtml.replace('&amp;','&')
    return renderhtml


