import settings

import print_common


class Mysql:

    def __init__(self, ip, port) -> None:
        super().__init__()
        self.ip = ip
        self.port = port

    def get_info(self):
        return f'ip:{self.ip},port:{self.port}'

    @classmethod
    def create_mysql_by_conf(cls):
        print(cls)
        return cls(settings.IP, settings.PORT)

    @staticmethod
    def create_id():
        import uuid
        return uuid.uuid4()


class Dameng(Mysql):
    pass


db = Mysql.create_mysql_by_conf()
# res = db.get_info()
# print(res)
# dm = Dameng.create_mysql_by_conf()

re1 = Mysql.create_id()
print(Mysql.create_id)
print(db.get_info)
