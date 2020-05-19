from flask import Flask,render_template,url_for,flash,redirect
from web_database.get_posts import Get_Blogs,Get_Portfolio
from web_database.posts_upload import BlogPost
from form import LoginForm , AdminPannelForm, BlogForm
from random import randint

def get_adminkey():
    return hex(randint(0,9**64))[2:]


global adminkey
adminkey = get_adminkey()

app = Flask(__name__)
app.config['SECRET_KEY']="withsj key is here"

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

@app.route("/<string:getkey>",methods=['GET','POST'])
def adminpannel(getkey):
    global adminkey
    form = AdminPannelForm(),BlogForm()

    if getkey == adminkey:
        if form[1].submit.data == True:
            date = str(form[1].year.data +"-"+ str(form[1].month.data) +"-"+ str(form[1].day.data))
            BlogPost(form[1].title.data,date,form[1].post.data).upload()
            return render_template('adminpannel.html',form=form)
        
        
        if form[0].logout.data == True:
            adminkey = get_adminkey()
            return redirect(url_for("home"))
        
        
        return render_template('adminpannel.html',form=form)
    return redirect(url_for("home"))

@app.route("/admin",methods=['GET','POST'])
def admin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "WithSJ" and form.password.data == "qwerty1234":
            global adminkey
            adminkey = adminkey = get_adminkey()
            flash(f"{form.username.data} you are log in now...","success")
            return redirect("/" + adminkey)        
    return render_template('admin.html',form=form)

@app.route("/blogs/<string:name>")
def blogpage(name):
    return render_template('blogpage.html',name=name)
    

if __name__ == "__main__":
    app.run(debug=True)