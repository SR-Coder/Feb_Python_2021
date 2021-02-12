from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is the base route "/"'

@app.route('/play')
def playground():
    return render_template('index.html', blockNumber=3, blockColor="blue")

@app.route('/play/<int:num>')
def dynamic_playground(num):
    return render_template('index.html', blockNumber=num, blockColor="Blue")

@app.route('/play/<int:num>/<color>')
def dynamic_playground_Wcolor(num, color):
    return render_template('index.html', blockNumber=num, blockColor=color)


@app.route('/play/<int:x>/<int:y>/<color1>/<color2>')
def quaziChecker(x,y,color1, color2):
    return render_template('board.html', width=x, height=y, blockColor1=color1, blockColor2=color2)



if __name__=="__main__":
    app.run(debug=True)