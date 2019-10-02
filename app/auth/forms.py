from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import Writer

class LoginForm(FlaskForm):
    email = StringField('Enter your email address',validators=[Required(),Email()])
    password = PasswordField('Fill in your password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Enter your email address',validators=[Required(),Email()]) 
    username = StringField('Enter your username',validators=[Required()]) 
    password = PasswordField('Password',validators=[Required(),EqualTo('password_confirm',message="Passwords must match")]) 
    password_confirm = PasswordField('Confirm Passwords',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if Writer.query.filter_by(email =data_field.data).first():
                raise ValidationError('That email is already registered')

    def validate_username(self,data_field):
        if Writer.query.filter_by(name = data_field.data).first():
            raise ValidationError('That username is already taken please use another')
 