import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='rBCL2HO6Onn27yl3', charset='utf8'
                       , database='myplus')
print(conn)
cs = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from sys_teacher;'
res = cs.execute(query=sql)  # 这里获取数据的总条数
print(cs.fetchall())  # 拿到全部的数据
# print(cs.fetchone())  # 只拿一条
# print(cs.fetchmany(2))  # 只拿2条
