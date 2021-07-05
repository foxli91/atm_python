'''
存放用户视图层
'''


# 1 注册功能
def register():
    print('1 注册功能')


# 2 登录功能
def login():
    print('2 登录功能')


# 3 查看余额功能
def check_balance():
    print('3 查看余额功能')


# 4 提现功能
def withdraw():
    print('4 提现功能')


# 5 还款功能
def pay_back():
    print('5 还款功能')


# 6 转账功能
def trans():
    print('6 转账功能')


# 7 查看流水功能
def check_money_log():
    print('7 查看流水功能')


# 8 购物功能
def shopping():
    print('8 购物功能')


# 9 查看购物车
def show_shopping_car():
    print('9 查看购物车')


# 10 管理员功能
def admins():
    print('10 管理员功能')


menu_dic = {
    '0': ['退出'],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['查看余额', check_balance],
    '4': ['提现', withdraw],
    '5': ['还款', pay_back],
    '6': ['查看流水', check_money_log],
    '7': ['转账', trans],
    '8': ['购物', shopping],
    '9': ['查看购物车', show_shopping_car],
    '10': ['管理', admins]

}
while True:
    for k in menu_dic:
        print("#" + k + ":" + menu_dic[k][0])
    ins = input('输入的选项是:')
    if ins == '0':
        break
    elif ins not in menu_dic:
        print('你输入的内容错误，请重新输入')
    else:
        # 这里是获取函数的地址 然后使用小括号是直接调用
        menu_dic[ins][1]()
