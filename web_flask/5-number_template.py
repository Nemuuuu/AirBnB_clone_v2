#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
app.strict_slashes=False

@app.route('/')
def hello():
    """ display Hello HBNB! """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """ display HBNB"""
    return "HBNB"

@app.route('/c/<text>')
def c(text):
    """display “C ” followed by the value of the text variable (replace underscore _ symbols with a space"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    """ display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>')
def number(n):
    """display “n is a number” only if n is an integer"""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

