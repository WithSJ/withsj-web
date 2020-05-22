from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,BooleanField,TextAreaField,FileField
from wtforms.validators import DataRequired,Length,Email

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=5,max=25)])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class BlogForm(LoginForm):
    title = StringField('Title',validators=[DataRequired(),Length(min=5,max=60)])
    day = SelectField('Day',choices=[_ for _ in range(1,32)])
    month = SelectField('Month',choices=[_ for _ in range(1,13)])
    year = SelectField('Year',choices=[_ for _ in range(2020,2071)])
    autodate = BooleanField('Auto Date')
    post = TextAreaField('Blog Post',validators=[DataRequired()])
    blogimage = FileField("Image")
    submit = SubmitField('Upload')

class AdminPannelForm(FlaskForm):
    logout = SubmitField("Logout")
