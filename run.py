
from withsj import app,get_adminkey,rendered_to_html
from flask import render_template,url_for,flash,redirect
from web_database.get_posts import Get_Blogs,Get_Portfolio,Get_Blogpage
from web_database.posts_upload import BlogPost
from withsj.form import LoginForm , AdminPannelForm, BlogForm
from datetime import datetime

USERNAME="WithSJ"
PASSWORD="qwerty1234"

global adminkey
adminkey = get_adminkey()

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
    # imagefile = os.path.join(app.root_path,"/static/images",blogid)
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
        
        # Preview Blog 
        if form["blog_form"].preview.data == True:

            # GEt Date
            if form["blog_form"].autodate.data == True:
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                date = str(form["blog_form"].year.data +"-"+ str(form["blog_form"].month.data) +"-"+ str(form["blog_form"].day.data))
            # End Geting Date

            data = {
                "title" : form["blog_form"].title.data, 
                "date" :  date,
                "post" : form["blog_form"].post.data
            }
            return rendered_to_html(render_template('blogpage.html',data=data))


        # End Preview Blog
        
        # Submit Blog Post here 
        if form["blog_form"].submit.data == True:
            
            imagedata = form["blog_form"].blogimage.data
            # GEt Date
            if form["blog_form"].autodate.data == True:
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                date = str(form["blog_form"].year.data +"-"+ str(form["blog_form"].month.data) +"-"+ str(form["blog_form"].day.data))
            # End Geting Date
            
            BlogPost(form["blog_form"].title.data, date, form["blog_form"].post.data,image=imagedata).upload() #upload post to database
            return render_template('adminpannel.html',form=form)
        # End Submit Blog Post
        
        if form["admin_pannel"].logout.data == True:
            adminkey = get_adminkey() #change Admin Pannel Link
            return redirect(url_for("home"))
        return render_template('adminpannel.html',form=form)
    
    else:
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