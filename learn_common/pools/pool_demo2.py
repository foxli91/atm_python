from concurrent.futures import ProcessPoolExecutor, Future
from threading import current_thread
from learn_common.print_common import ps, time_str
import time
import random
import os

'''
#   默认的构造方法里面是传数字的，不传的话会默认设置加载cpu个数*5的进程数
#   如果传了数字5那么 这个进程池里面只有5个线程来反复使用
#   使用方法，将任务提交到池子里面
'''
process_pool = ProcessPoolExecutor()


def select_money(user_id: str) -> float:
    # 模拟休眠一下
    sleep = random.randint(0, 10)
    print(f'[当前时间{time_str()}]--[用户id：{user_id}]---[sleep休眠的时间:{sleep}]---[当前进程ID：{os.getpid()}]')
    time.sleep(sleep)
    return float(sleep ** 2)


def result_back(res: Future) -> float:
    moneys = res.result()
    print(f'获取的金钱是{moneys}')
    return moneys


if __name__ == '__main__':
    ps()

    for i in range(10):
        ids = f'usi{i}'
        process_pool.submit(select_money, ids).add_done_callback(result_back)
