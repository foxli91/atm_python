from multiprocessing import Process
from learn_common.print_common import ps, time_str
import os


def tak():
    print(f'task执行的时间{time_str()}')
    import time
    time.sleep(2)
    print(f'子进程的进程id号码是：{os.getpid()}')


if __name__ == '__main__':
    p = Process(target=tak, args=())
    ps()
    print(f'主进程开始了我的进程id号码是：{os.getpid()}')
    p.daemon = True
    p.start()
    # p.terminate()
    p.is_alive()
    p.join()
    print(f'主进程结束了我的进程id号码是：{os.getpid()}')

info = {
    'user_name': '张三',
    'age': 45,
    'address': '北京市朝阳区'
}
value = info.get('user_name')
print(value)
