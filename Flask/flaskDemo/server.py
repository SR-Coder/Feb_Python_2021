from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def dashboard():
    return 'Hey good job you did it'

@app.route('/firstTemplate')
def hello_template():
    return render_template('index.html', name='John', age=25)

@app.route('/firstTemplate/<name1>/<age1>')
def hello_template_wArgs(name1, age1):
    return render_template('index.html', name=name1, age=age1)

if __name__=="__main__":
    app.run(debug=True)