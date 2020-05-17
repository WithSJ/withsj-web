from flask import Flask,render_template,url_for
from web_database.get_posts import Get_Blogs,Get_Portfolio
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/blogs")
def blogs():
    data_list = Get_Blogs().data()
    return render_template('blogs.html',data_list=data_list)

@app.route("/portfolio")
def portfolio():
    data_list = Get_Portfolio().data()
    return render_template('portfolio.html',data_list=data_list)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blogs/<string:name>")
def blogpage(name):
    return render_template('blogpage.html',name=name)
    

if __name__ == "__main__":
    app.run(debug=True)