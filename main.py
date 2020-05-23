
from flask import Flask,render_template,url_for,flash,redirect
from web_database.get_posts import Get_Blogs,Get_Portfolio,Get_Blogpage
from web_database.posts_upload import BlogPost
from form import LoginForm , AdminPannelForm, BlogForm
from random import randint
from datetime import datetime

USERNAME="WithSJ"
PASSWORD="qwerty1234"

def get_adminkey():
    return hex(randint(0,9**64))[2:]

def rendered_to_html(renderhtml):
    renderhtml= renderhtml.replace('&lt;','<')
    renderhtml = renderhtml.replace('&gt;','>')
    renderhtml = renderhtml.replace('&#34;','"')
    renderhtml = renderhtml.replace('&#39;',"'")
    renderhtml = renderhtml.replace('&amp;','&')
    return renderhtml

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
    if data_list == None:
        return render_template('blogs.html')

    return render_template('blogs.html',data_list=data_list)

@app.route("/blogs/<blogid>")
def blogpage(blogid):
    data = Get_Blogpage(blogid).data()
    return rendered_to_html(render_template('blogpage.html',data=data))

@app.route("/portfolio")
def portfolio():
    data_list = Get_Portfolio().data()
    return render_template('portfolio.html',data_list=data_list)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/<getkey>",methods=['GET','POST'])
def adminpannel(getkey):
    global adminkey
    form = {"admin_pannel":AdminPannelForm(),"blog_form":BlogForm()}

    if getkey == adminkey:
        if form["blog_form"].submit.data == True:
            
            if form["blog_form"].autodate.data == True:
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                date = str(form["blog_form"].year.data +"-"+ str(form["blog_form"].month.data) +"-"+ str(form["blog_form"].day.data))
            
            BlogPost(form["blog_form"].title.data, date, form["blog_form"].post.data).upload()
            return render_template('adminpannel.html',form=form)
        
        
        if form["admin_pannel"].logout.data == True:
            adminkey = get_adminkey()
            return redirect(url_for("home"))
        
        
        return render_template('adminpannel.html',form=form)
    return redirect(url_for("home"))

@app.route("/admin",methods=['GET','POST'])
def admin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == USERNAME and form.password.data == PASSWORD:
            global adminkey
            adminkey = adminkey = get_adminkey()
            flash(f"{form.username.data} you are log in now...","success")
            return redirect("/" + adminkey)        
    return render_template('admin.html',form=form)


    

if __name__ == "__main__":
        app.run(debug=True)