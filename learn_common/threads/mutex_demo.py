from multiprocessing import Process, Lock, synchronize,Queue

from learn_common.print_common import ps, time_str
import random
import time
import os


def buy_ticket(num: int, mute: synchronize.Lock) -> str:
    # 模拟获取票的数量
    print(f'{time_str()}我是{os.getpid()}开始买票了，我马上查询')
    tk = random.randint(0, 20)
    print(f'查询到的票是%d张' % tk)
    # 枪锁
    mute.acquire()
    print(f'{time_str()}我是进程{os.getpid()}拿到锁了')
    time.sleep(tk)
    # 抢到了买票默认只能买一张
    if tk == 0:
        return '没有票了'
    tk -= num
    # 释放锁
    print(f'我是进程{os.getpid()}释放锁了')
    mute.release()


import queue

# 指定队列的大小
q = queue.Queue(5)
# 如果队列满了会阻塞住放不进去，直到等到有空余的位置
q.put(5)
# 队列先进先出，这里是取数据，默认get()不传参数会死等，直到等到数据
q.get()
# 这里是等待3秒，没有等到数据会报错，需要try expect
q.get(timeout=3)
# 这里是取只要没有取到就会报错
q.get_nowait()
# 判断是不是满的
q.full()
# 判断是不是空的
q.empty()











if __name__ == '__main__':
    ps()
    mutex = Lock()
    u1 = Process(target=buy_ticket, args=(1, mutex))
    u2 = Process(target=buy_ticket, args=(1, mutex))
    print(f'买票开始执行的时间{time_str()}')
    u1.start()
    u2.start()
    u1.join()
    u2.join()
