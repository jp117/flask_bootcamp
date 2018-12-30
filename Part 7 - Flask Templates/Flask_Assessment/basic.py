from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/username')
def username():
    username = request.args.get('username')
    capital = 'fail'
    lowercase = 'fail'
    number = 'fail'
    if any(letter.isupper() for letter in username):
        capital = 'passed'
    if any(letter.islower() for letter in username):
        lowercase = 'passed'
    if username[-1].isdigit():
        number = 'passed'
    return render_template('username.html', capital=capital, lowercase=lowercase, number=number)


if __name__ == '__main__':
    app.run()