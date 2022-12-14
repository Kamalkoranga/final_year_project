from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User, Upload

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class CommentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired(), Length(min=0, max=200)])
    submit = SubmitField('Comment')

class UploadFile(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description')
    code = TextAreaField(validators=[DataRequired()])
    filename = StringField('File name (with extension)', validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_filename(self, filename):
        file = Upload.query.filter_by(filename=filename.data).first()
        if file is not None:
            raise ValidationError('Please use a different filename')

class EditFileForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description')
    code = TextAreaField(validators=[DataRequired()])
    filename = StringField('File name (with extension)', validators=[DataRequired()])
    submit = SubmitField('Save')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
