from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Future
from threading import current_thread
from learn_common.print_common import ps, time_str
import time
import random

'''
#   默认的构造方法里面是传数字的，不传的话会默认设置加载cpu个数*5的线程数
#   如果传了数字5那么 这个线程池里面只有5个线程来反复使用
#   使用方法，将任务提交到池子里面
'''
thread_pool = ThreadPoolExecutor(5)


def select_money(user_id: str) -> float:
    # 模拟休眠一下
    sleep = random.randint(0, 10)
    print(f'[当前时间{time_str()}]--[用户id：{user_id}]---[sleep休眠的时间:{sleep}]---[当前线程ID：{current_thread().ident}]')
    time.sleep(sleep)
    return float(sleep ** 2)


def result_back(res: Future) -> float:
    moneys = res.result()
    print(f'获取的金钱是{moneys}')
    return moneys


ps()
# res = select_money('1232344')
# print(f'得到的金钱是{res}')
if __name__ == '__main__':

    for i in range(10):
        ids = f'usi{i}'
        thread_pool.submit(select_money, ids).add_done_callback(result_back)

# result_list = []
# for i in range(10):
#     ids = f'usi{i}'
#     res = thread_pool.submit(select_money, ids)
#     result_list.append(res)
#
# for s in result_list:
#     print(f'类型是{type(s)}')
#     res = s.result()
#     print(f'获得的结果是{res}')
