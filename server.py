from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/play/')
def play1():
    num = 3
    color = "lightblue"
    return render_template('play.html', num = num, color = color)

@app.route('/play/<int:num>/')
def play2(num):
    color = "lightblue"
    return render_template('play.html', num = num, color = color)


@app.route('/play/<int:num>/<string:color>/')
def play3(num, color):
    return render_template('play.html', num = num, color = color)

if __name__=="__main__":
    app.run(debug=True)