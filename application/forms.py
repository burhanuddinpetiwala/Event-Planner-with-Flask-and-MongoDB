from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User

class LoginForm(FlaskForm):
    Email = StringField("Email", validators=[DataRequired(), Email()])
    Password = StringField("Password", validators=[DataRequired(), Length(min = 8, max = 21)])
    Remeber_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    First_Name = StringField("First Name", validators=[DataRequired(), Length(min = 2, max = 72)])
    Last_Name = StringField("Last Name", validators=[DataRequired(), Length(min = 2, max = 72)])
    Email = StringField("Email", validators=[DataRequired(), Email()])
    Password = StringField("Pasword", validators=[DataRequired(), Length(min = 8, max = 21)])
    Password_confirm = StringField("Confirm Pasword", validators=[DataRequired(), Length(min = 8, max = 21), EqualTo('Password')])
    submit = SubmitField("Register")

    def validate_email(self, Email):
        user = User.objects.get(Email=Email.data).first()
        if user:
            raise ValidationError("Email is already in use!")

class EventForm(FlaskForm):
    Event_Name = StringField("Event Name", validators=[DataRequired()])
    Event_Date = DateField("Event Date", validators=[DataRequired()])
    submit = SubmitField("Schedule Event")

class UpdateForm(FlaskForm):
    Event_Name = StringField("Event Name", validators=[DataRequired()], value = "Hello")
    Event_Date = DateField("Event Date", validators=[DataRequired()])
    submit = SubmitField("Schedule Event")

