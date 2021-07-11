from multiprocessing import Process
from learn_common.print_common import ps, time_str

money=1500

def futask(name, age):
    print('进程开始启动执行了......')
    print('hello这是进程的创建name=%s ,age=%d' % (name, age))
    print(f'task暂停时间{time_str()}')
    import time
    time.sleep(5)
    print(f'task结束时间{time_str()}，进程执行完毕了......')


if __name__ == '__main__':
    ps()
    tak = Process(target=futask, args=('张三', 15))
    tak2 = Process(target=futask, args=('李四', 35))
    tak3 = Process(target=futask, args=('王五', 28))
    print(f'开始时间{time_str()}')
    tak.start()
    tak2.start()
    tak3.start()
    tak.join()
    tak2.join()
    tak3.join()
    print(f'主进程开始执行完毕了{time_str()}')
