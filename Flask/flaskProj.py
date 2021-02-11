from flask import Flask # this imports all the methods assiciated with flask
app = Flask(__name__)

@app.route('/') # base route http://localhost:5000
def hello_world():
    return 'Hello World'

@app.route('/say_hello') # http://localhost:5000/say_hello
def say_hello():
    return "Hello friend... welcome and thanks for stopping by"

@app.route('/say_hello/<name>')
def personal_hello(name):
    return f'Hello {name}.... thanks for stopping by'

@app.route('/say_hello/<name>/<grade>')
def hello_plus(grade, name):
    return f'Hello {name}, your new grade is an {grade}'


if __name__=='__main__':
    app.run(debug=True)