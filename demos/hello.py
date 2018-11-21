from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
@app.route('/')
def index():
    return "<h> hello </h>"


@app.route('/welcome/<name>')
def welcome(name):
    return "<h> hello %s" % name


app.run(host='0.0.0.0', port=1024)
