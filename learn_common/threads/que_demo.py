from multiprocessing import Queue, Process,JoinableQueue
from learn_common.print_common import ps


def producer(q: Queue):
    q.put('模拟从数据库取查数据')


def consumer(q: Queue):
    print(f'我是消费者我要从队列里面取数据{q.get()}')


if __name__ == '__main__':
    # 主进程从子进程里面拿数据
    q = Queue(5)
    t1 = Process(target=producer, args=(q,))
    t2 = Process(target=consumer, args=(q,))
    t1.start()
    t2.start()
    # 这里拿不到会死等
    ps()
    # print(f'我是主进程我拿到的数据是{q.get()}')
