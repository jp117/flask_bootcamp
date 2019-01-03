from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    pupid = IntegerField('ID of puppy that got adopted')
    name = StringField('Name of owner')
    submit = SubmitField('Add owner')
