# 对应'account'表
class Account:
    def __init__(self):
        self.name = 'account'
        self.password = 'password'


# self.accountExist = 'sorry,the account has exist'
# self.accountnoExist = 'sorry,the account has not exist'
# self.register_success = 'register success'
# self.login_success = 'login success'
# self.error = 'error'

# def register(self, accountNumber, password):
#     if r.hexists(self.name, accountNumber):
#         return self.accountExist
#     else:
#         if r.hset(self.name, accountNumber, password):
#             return self.register_success
#         else:
#             return self.error
#
# def login(self, accountNumber, password):
#     expected = r.hmget(self.name, accountNumber)
#     if str(password) == str(expected[0]):
#         return self.login_success
#     else:
#         return self.error

# 每一个account就是一个表
class Rank:
    def __init__(self):
        self.bald_count = 0  # 被剃头次数
        self.haircut_count = 0  # 剃头次数
        self.score = 0  # 积分数


class Admin:
    account = 'admin'
