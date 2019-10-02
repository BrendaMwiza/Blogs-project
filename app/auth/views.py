from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,login_required,logout_user
from . import auth
from .. import db
from ..models import Writer
from .forms import RegistrationForm,LoginForm
from ..email import mail_message
from werkzeug.security import check_password_hash



@auth.route('/login',methods=['GET','POST'])
def login():
    '''
    Function that checks if the form is validated
    '''

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Writer(email=login_form.email.data)
        user = Writer.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))

        flash('invalid username or password')

    return render_template('auth/login.html',login_form=login_form)


@auth.route('/register',methods=['GET','POST'])
def register():
    '''
    Registration function
    '''

    form =RegistrationForm()
    if form.validate_on_submit():
        user =Writer(email=form.email.data,name=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        try:
            message = Message("Hello Welcome to the blog post",sender=("Blogs","brendabrizy@gmail.com"),recipients=[form.email.data])
            mail.send(message)
        except Exception as e:
            print("email not sent")
        return redirect(url_for('auth.login'))

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form=form)

#logout function
@auth.route('/logout') 
@login_required 
def logout(): 
    logout_user()
    return redirect(url_for('main.index'))