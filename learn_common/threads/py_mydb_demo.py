import pymysql

conn = pymysql.connect(host='172.16.10.145', port=3306, user='root', passwd='123456', db='hello_mydatas')
cu = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from t_areas'

res=cu.execute(sql)
print(cu.fetchall())