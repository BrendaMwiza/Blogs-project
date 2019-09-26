from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,RadioField,SubmitField,SelectField,ValidationError
from wtforms.validators import Required

#Blog Form
class BlogForm(FlaskForm):
    title = StringField('Post Your Blog')
    body = TextAreaField('Body', validators=[Required()])
    submit = SubmitField('Submit Blog')

#Comment Form
class CommentForm(FlaskForm):
    body = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()

#Subscription Form
class SubscriptionForm(FlaskForm):
    email = TextAreaField('Email')
    submit = SubmitField()

    def validate_email(self,field):
        if SubscriptionForm.query.filter_by(email=field.data).first():
            raise ValidationError('Email exists')

class UpdateBlog(FlaskForm):
    body = TextAreaField("Update Blog", validators=[Required()])
    submit = SubmitField('Post')