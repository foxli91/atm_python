from gevent import monkey

monkey.patch_all()
from gevent import spawn
from learn_common.print_common import ps, time_str
import time


def io_test1(name: str) -> str:
    print(f'hello{name}')
    time.sleep(3)
    return f'你好呢......{name}'


if __name__ == '__main__':
    ps()
    res = spawn(io_test1, '是你爹')
    # 返回的是一个<class 'gevent._gevent_cgreenlet.Greenlet'>
    print(type(res))
    res.join()
    # 通过get来获取结果
    s = res.get()
    print(s)
