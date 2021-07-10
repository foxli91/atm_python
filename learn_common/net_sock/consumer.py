import socket

ip_port = ('127.0.0.1', 9000)
BUF_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect_ex(ip_port)  # 开始按照ip连接

s.send('我是服务端我开始发送消息了，is牛逼'.encode('utf-8'))  # 发消息,说话(只能发送字节类型)

feedback = s.recv(BUF_SIZE)  # 接收服务端发来的消息
print(feedback.decode('utf-8'))

s.close()  # 客户端关闭
