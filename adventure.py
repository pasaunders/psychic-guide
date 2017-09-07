from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
@app.route('/')
def begin():
    # if request.method == 'POST':
    #     return redirect(url_for())
    return render_template('begin.html')


@app.route('/right')
def right():
    return render_template('right.html')


@app.route('/left')
def left():
    return render_template('left.html')


@app.route('/red')
def red():
    return render_template('red.html')


@app.route('/black')
def black():
    return render_template('black.html')


app.run(debug=True)
