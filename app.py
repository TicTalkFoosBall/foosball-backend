import os
import redis
from flask import Flask, request, jsonify, make_response, session
from jinja2 import escape


def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.session_cookie_name = 'encryptCookie'
app.after_request(after_request)
redis = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)


@app.before_first_request
def beforeFirstRequest():
    session.permanent = True


@app.route('/welcome')
@app.route('/')
def index():
    return "<h> hello </h>"


@app.route('/get')
def testGet():
    """
    ex: http://localhost:5000/get?name=ice
    """
    # name = escape(request.args.get('name'))
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('account')
    if name:
        return 'name = {}'.format(escape(name))
    else:
        return jsonify(msg='name为空', code='404'), 404


@app.route('/cookie')
def testCookie():
    # 未加密
    # response = make_response(redirect(url_for('index')))
    response = make_response()
    response.set_cookie('account', 'ice')

    # 加密
    session['encryptAccount'] = 'encryptIce'  # Flask再视图函数结束时会将session中的值都传递到客户端
    # session.pop('encryptAccount')
    # abort(403)
    return response


@app.route('/register', methods=['POST'])
def register():
    account = request.form['account']
    password = request.form['password']
    if redis.hexists('account', account):
        return jsonify(msg='注册失败,账号已存在!'), '100'
    else:
        if redis.hset('account', account, password):
            session['account'] = account
            session['password'] = password
            return jsonify(msg='注册成功!')
        else:
            return jsonify(msg='redis存储失败')


@app.route('/login', methods=['POST'])
def login():
    account = request.form['account']
    password = request.form['password']
    accountFromRedis = redis.hget('account', account)
    if str(password) == str(accountFromRedis):
        session['account'] = account
        session['password'] = password
        return jsonify(msg='登录成功')
    else:
        return jsonify(msg='账号密码不匹配')


@app.route('/rank', defaults={'account': 'all'}, methods=['GET'])
@app.route('/rank/<account>', methods=['GET'])
def rank(account):
    def getRankData(fun_account):
        fun_result = redis.hgetall('account:%s' % fun_account)
        if fun_result.get('bald_count') is None:
            fun_result['bald_count'] = 0
        if fun_result.get('haircut_count') is None:
            fun_result['haircut_count'] = 0
        if fun_result.get('score') is None:
            fun_result['score'] = 0
        return {
            'bald_count': fun_result['bald_count'],
            'haircut_count': fun_result['haircut_count'],
            'score': fun_result['score'],
            'account': fun_account
        }

    if str(account) == str('all'):
        resultDic = []
        for item_account in redis.hkeys('account'):
            resultDic.append(getRankData(item_account))
            print('account = %s' % item_account)
        return jsonify(resultDic)
    else:
        return jsonify(getRankData(account))


if __name__ == '__main__':
    app.run()

#
#
# custom cli
import click


@app.cli.command()
def sayHello():
    """
    just say hello
    """
    click.echo('hello')
