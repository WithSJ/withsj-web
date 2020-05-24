
from flask import Flask
from random import randint


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


