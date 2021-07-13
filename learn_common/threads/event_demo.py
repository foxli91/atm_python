from threading import Thread, Event
import time
from learn_common.print_common import ps, time_str

eve = Event()


def lights():
    print(f'{time_str()}红灯亮起来了请稍等')
    time.sleep(10)
    print(f'{time_str()}绿灯亮了')
    eve.set()


def cars(name):
    print('我是%s,我在等红灯' % name)
    # 一旦event.set()执行完毕大家都会从这里释放
    eve.wait()
    print('%s跑了' % name)


if __name__ == '__main__':
    t1 = Thread(target=lights)
    ls = []
    ps()
    for i in range(10):
        t = Thread(target=cars, args=(f'{i}',))
        t.start()
        ls.append(t)
    t1.start()
    for i in ls:
        i.join()
