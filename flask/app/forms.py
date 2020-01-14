from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    date = StringField('Input a website for a facebook page', validators=[DataRequired()])
    submit = SubmitField('Analyze!!!')