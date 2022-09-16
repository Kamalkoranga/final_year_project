from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired, Email, EqualTo
from app.models import User
from flask import flash

class RegisterForm(FlaskForm):
    # username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username", "class": "input"})
    # password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password", "class": "input"})
    # submit = SubmitField('Sign Up')

    # def validate_username(self, username):
    #     user = username.data.lower()
    #     existing_user_username = User.query.filter_by(username=user).first()
    #     if existing_user_username:
    #         flash('That username already exists. Please choose a different one.')
    #         raise ValidationError('That username already exists. Please choose a different one.')

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
class LoginForm(FlaskForm):
    # username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"autocomplete": "username", "id": "login__username", "type": "text", "class": "form__input", "placeholder": "Username"})
    # password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"id": "login__password", "type": "password", "class": "form__input", "placeholder": "Password"})
    # submit = SubmitField('Login')
    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')