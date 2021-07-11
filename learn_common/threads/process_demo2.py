from multiprocessing import Process
from learn_common.print_common import ps, time_str

money = 1500


def futask():
    global money
    print('子进程开始启动执行了......')
    import time
    time.sleep(5)
    money = 9000

    print(f'task结束时间{time_str()}，进程执行完毕了......')
    print('子进程中money最后是多少呢？money=%d' % money)


if __name__ == '__main__':
    ps()
    tak = Process(target=futask, args=())
    # tak2 = Process(target=futask, args=())
    # tak3 = Process(target=futask, args=())
    print(f'开始时间{time_str()}')
    tak.start()
    # tak2.start()
    # tak3.start()
    tak.join()
    # tak2.join()
    # tak3.join()
    print('主进程之中的money是多少呢? money=%d' % money)
    print(f'主进程开始执行完毕了{time_str()}')
