from threading import Thread, current_thread
from learn_common.print_common import ps

money = 100


def task(name):
    print('我是线程打印的thread，我的name是=%s' % name)


def change_money():
    global money
    money = 7777
    print(money)
    print(current_thread().name, current_thread().native_id)


if __name__ == '__main__':
    # t = Thread(target=task, args=('张三',))
    # t.start()
    ps()
    t = Thread(target=change_money)
    t.start()
    t.daemon = True
    t.join()
    print('主进程执行完毕')
    print(money)
