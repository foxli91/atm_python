from multiprocessing import Process, current_process,synchronize
from learn_common.print_common import ps, time_str

def tak():
    print(f'task执行的时间{time_str()}')
    import time
    time.sleep(2)
    print(f'子进程的进程id号码是：{current_process().pid}')


if __name__ == '__main__':
    p = Process(target=tak, args=())
    ps()
    print(f'主进程开始了我的进程id号码是：{current_process().pid}')
    p.start()
    p.join()
    print(f'主进程结束了我的进程id号码是：{current_process().pid}')
