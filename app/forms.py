from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired


class CreateUserForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    role_id = RadioField("Role", choices=[("1", "User"), ("2", "Moderator")], default=1)
    submit = SubmitField("Sign In")
