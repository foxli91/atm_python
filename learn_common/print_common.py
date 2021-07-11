
def ps():
    print('-' * 25 + '执行完毕' + '-' * 25)

def time_str()->str:
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S')


# import datetime
#
# nod = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(nod)


# import  time
# print(time.strptime('1992-06-12 15:16:30', '%Y-%m-%d %H:%M:%S'))
# st=time.strptime('1992-06-12 15:16:30', '%Y-%m-%d %H:%M:%S')
# year=st.tm_year
# month=st.tm_mon
# day=st.tm_mday
# hour=st.tm_hour
# mins=st.tm_min
# second=st.tm_sec
# week=st.tm_wday
# print(type(st))
# print('年',year)
# print('月',month)
# print('日',day)
# print('时',hour)
# print('分',mins)
# print('秒',second)
# print('星期',week)
