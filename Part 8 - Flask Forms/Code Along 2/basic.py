from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (SubmitField, StringField, BooleanField, DateTimeField, RadioField, SelectField, TextField,
                     TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):

    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered', validators=[DataRequired()])
    mood = RadioField('Please choose your mood:', choices=[
        ('mood one:', 'Happy'), 'mood two:', 'Excited'])
    food_choice = SelectField(u'Pick your favorite food:', choices=[
        ('chi', 'Chicken'), ('bf', 'Beef'), ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyou'))
    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == "__main)__":
    app.run(debug=True)
