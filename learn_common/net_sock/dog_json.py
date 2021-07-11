import os, sys

sys.path.append(os.pardir)
from learn_common.print_common import ps
from learn_common.dog import Dog
import json

ps()
doo = Dog('李小华', 3)
# print(doo)
# json.dumps(doo)
res = json.dumps(doo, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
print(res)
