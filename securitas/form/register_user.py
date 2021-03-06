from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class RegisterUserForm(FlaskForm):
    firstname = StringField(
        'First Name', validators=[DataRequired(message='First name must not be empty')]
    )

    lastname = StringField(
        'Last Name', validators=[DataRequired(message='Last name must not be empty')]
    )

    username = StringField(
        'Username',
        validators=[DataRequired(message='User name must not be empty')],
        description="No spaces please",
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message='Password must not be empty'),
            EqualTo('password_confirm', message='Passwords must match'),
        ],
        description="Please choose a strong password",
    )

    password_confirm = PasswordField('Confirm Password')
