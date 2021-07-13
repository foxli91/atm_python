from multiprocessing import Process, RLock, Lock
from threading import Semaphore

# mutexA=mutexB=RLock()

sm = Semaphore(5)  # 容量


def ts():
    # 抢锁
    sm.acquire()

    print('业务......')
    # 释放锁
    sm.release()


class MyProcess(Process):
    def run(self) -> None:
        print('第二种方式运行')
        import time
        time.sleep(10)
        print('第二种方式执行完毕了')


if __name__ == '__main__':
    my = MyProcess()
    my.start()
    print('主进程在执行了')
