from flask import render_template
# ,request,redirect,url_for,flash,abort
from . import main
from .. import db
# from .forms import BlogForm, CommentForm, SubscriptionForm
from ..models import User,Writer,Blog,Comment,Subscription
from flask_login import login_required,current_user
# from app import login_manager

# @login_manager.user_loader
# def load_user(user_id):
#     '''
#     @login_manager.user_loader Passes in a writer_id to this function
#     Function queries the database and gets a user's id as a response
#     '''
#     return User.query.get(user_id)

#Views
@main.route('/')
def index():

    blogs=blog.query.all()

    return render_template('index.html', blogs=blogs)

# @main.route('/blog', methods=['GET','BLOG'])
# def new_blog():
#     '''
#     New Blog Page
#     '''
#     blog_form = BlogForm()

#     if blog_form.validate_on_submit():
#         title = blog_form.title.data
#         body = blog_form.body.data


#         # updated review instance
#         new_blog = Blog(title=title,body = body)

#         #save review blog
#         new_blog.save_blog()
#         return redirect(url_for('main.index'))

#     title = f'{blog.title}'
#     return render_template('blog.html',title= title, blog_form=blog_form)


# @main.route('/comments/<int:id>', methods=['GET', 'BLOG'])
# @login_required
# def comments(id):
#     comment_form = CommentForm()
#     comment = Comment.query.order_by('-id').all()

#     if comment_form.validate_on_submit():
#         comment = comment_form.comment.data()
#         new_comment = Comment(comment=comment,users=current_user.username)
#         new_comment.save_comment()
#         return redirect(url_for('main.comments',id = blog.id))
#     return render_template('comments.html')

# @main.route('/delete/<int:id>')
# @login_required
# def delete(id):
#     del_comment = Comment.query.get(id)
#     db.session.delete(del_comment)
#     db.session.commit()
#     return redirect(url_for('main.index'))

# @main.route('/subscription',methods = ["GET","BLOG"])
# def subscriber():

#     form= SubscriptionForm()


#     if form.validate_on_submit():
#         email = form.email.data
#         date = form.date.data


#         # updated review instance
#         new_subscriber = Subscription(email=email,date = date,user_id=current_user.id)

#         #save review method
#         new_subscriber.save_subscriber()
#         return redirect(url_for('subscriber'))


#     return render_template('index.html',email= email, subscribe_form=form )