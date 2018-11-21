# write_by :rick
import redis

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)


# Account structure is currently only account number: password.
# account structure's name is "account"
class Account:

    def __init__(self):
        self.name = 'account'
        self.accountExist = 'sorry,the account has exist'
        self.accountnoExist = 'sorry,the account has not exist'
        self.register_success = 'register success'
        self.login_success = 'login success'
        self.error = 'error'

    def register(self, accountNumber, password):
        if r.hexists(self.name, accountNumber):
            return self.accountExist
        else:
            if r.hset(self.name, accountNumber, password):
                return self.register_success
            else:
                return self.error

    def login(self, accountNumber, password):
        expected = r.hmget(self.name, accountNumber)
        if str(password) == str(expected[0]):
            return self.login_success
        else:
            return self.error


def testPython(self):
    return 'name'
