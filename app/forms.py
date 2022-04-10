# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[DataRequired()])
    photo = FileField('photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','Images Only'])])