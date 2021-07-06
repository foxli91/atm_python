'''
配置文件
'''
# 这里需要说明一下 台式机上传

tus = tuple(['1', '2'])
print(type(tus))
print(tus[0])
for i in tus:
    print(i)
abs = {
    'name': '张三',
    'age': 25,
    'address': [1, 2, 3, 4]
}

for k, v in abs.items():
    print(k, v)
    print(type(v))
    if type(v) == list:
        print('sssss')
