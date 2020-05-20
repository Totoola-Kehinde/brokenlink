from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,URL,Length, ValidationError


class UrlForm(FlaskForm):
    url = StringField("Input URL", validators=[DataRequired(),URL(require_tld=True), Length(min=5, max=10)])
    submit = SubmitField("Check")