from learn_common.print_common import ps

ps()
try:

    a = 1 / 5
    print(a)
except Exception as e:
    print(e)
else:
    print('未执行异常代码')
finally:
    print('无论是否检测到异常都会执行')
