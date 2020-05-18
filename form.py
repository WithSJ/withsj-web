from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=5,max=25)])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')
    
