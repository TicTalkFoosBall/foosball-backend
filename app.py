from flask import Flask
from account import Account

app = Flask(__name__)
accountManager = Account()


@app.route('/welcome')
@app.route('/')
def index():
    return "<h> hello </h>"


@app.route('/account/register/<string:accountnumber>/<string:password>')
def register(accountnumber, password):
    return accountManager.register(accountnumber, password)


@app.route('/account/login/<string:accountnumber>/<string:password>')
def login(accountnumber, password):
    return accountManager.login(accountnumber, password)


app.run()
