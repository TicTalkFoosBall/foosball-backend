from flask import Flask, request
import json
from account import Account

def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

app = Flask(__name__)
app.after_request(after_request)
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
