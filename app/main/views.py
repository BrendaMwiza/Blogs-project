from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from .. import db
from .forms import BlogForm, CommentForm, SubscriptionForm, UpdateProfile
from ..models import Writer,Blogs,Comment,Subscription
from flask_login import login_required,current_user
from app import login_manager
from ..requests import get_quote

@login_manager.user_loader
def load_user(writer_id):
    '''
    @login_manager.writer_loader Passes in a writer_id to this function
    Function queries the database and gets a writer's id as a response
    '''
    return Writer.query.get(writer_id)

#Views
@main.route('/')
def index():

    blogs=Blogs.query.all()

    grt_quote = get_quote('random_quotes')
    print(grt_quote)

    return render_template('index.html', blogs = blogs, random_quotes =  grt_quote )

@main.route('/blog', methods=['GET','POST'])
def new_blog():
    '''
    New Blog Page
    '''
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        title = blog_form.title.data
        body = blog_form.body.data


        # updated review instance
        new_blog = Blog(title=title,body = body)

        #save review blog
        new_blog.save_blog()
        return redirect(url_for('main.index'))

    title = f'{blog.title}'
    return render_template('index.html',title= title, blog_form=blog_form)


@main.route('/comments/<int:id>', methods=['GET', 'POST'])
@login_required
def comments(id):
    comment_form = CommentForm()
    comment = Comment.query.order_by('-id').all()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data()
        new_comment = Comment(comment=comment,users=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('main.comments',id = blog.id))
    return render_template('comments.html')

@main.route('/delete/<int:id>')
@login_required
def delete(id):
    del_comment = Comment.query.get(id)
    db.session.delete(del_comment)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/subscription',methods = ["GET","BLOG"])
def subscriber():

    form= SubscriptionForm()


    if form.validate_on_submit():
        email = form.email.data
        date = form.date.data


        # updated review instance
        new_subscriber = Subscription(email=email,date = date,user_id=current_user.id)

        #save review method
        new_subscriber.save_subscriber()
        return redirect(url_for('subscriber'))


    return render_template('index.html',email= email, subscribe_form=form )

@main.route('/writer/<uname>')
def profile(uname):
    writer = Writer.query.filter_by(username = uname).first()

    if writer is None:
        abort(404)

    return render_template("profile/profile.html", writer = writer)

@main.route('/writer/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    writer = Writer.query.filter_by(username = uname).first()
    if writer is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        writer.bio = form.bio.data

        db.session.add(writer)
        db.session.commit()

        return redirect(url_for('.profile',uname=writer.username))

    return render_template('profile/update.html',form =form)

@main.route('/writer/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    writer = Writer.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        writer.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('main.profile',uname=uname)) 
    return render_template('profile/update.html',form =form)