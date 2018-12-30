# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return '<h1> This is homepage.  Go to /puppy-latin/<name> to find your puppy\'s name in latin</h1>'

@app.route('/puppy-latin/<name>') # Fill this in!
def puppylatin(name):
    if name[-1] == 'y':
        plname = name[:-1] + 'iful'
        return f'<h1> Your dog\'s name is {name} and your dog\'s puppy-latin name is {plname}</h1>'
    else:
        return '<h1> Your dog\'s name is {} and your dog\'s puppy-latin name is {}</h1>'.format(name, name + 'y')

if __name__ == '__main__':
    app.run()