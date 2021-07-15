import pymysql
from learn_common.threads.entity.area_entity import Area
from learn_common.print_common import ps, time_str

conn = pymysql.connect(host='172.16.10.145', port=3306, user='root', passwd='123456', db='hello_mydatas',
                       charset='utf8')
cu = conn.cursor(cursor=pymysql.cursors.DictCursor)
# sql = 'select * from t_areas where id=%s and ara_name=%s'
#
# res = cu.execute(query=sql, args=(2, '西固区'))
sql = 'select * from t_areas'
insert_sql = 'insert into t_areas(ara_name,area_code) values (%s,%s)'

# res2 = cu.execute(query=insert_sql, args=('兰州市', '621000'))
res2 = cu.executemany(query=insert_sql,
                      args=[('武威市', '624000'),
                            ('张掖', '625000'), ('定西市', '627000')])
if res2:
    conn.commit()
else:
    conn.rollback()
res = cu.execute(query=sql)
res_list = cu.fetchall()
entity_list = []
# 这里将拿到的数据转换成实体对象
ps()


def get_area_list(area: []):
    for i in area:
        en = Area()
        for k, v in i.items():
            en.__setattr__(k, v)
        print(en)


get_area_list(res_list)
