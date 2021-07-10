import socket

i = 0
while True:
    ip_port = ('127.0.0.1', 9000)
    BUF_SIZE = 1024
    consumer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    consumer.connect_ex(ip_port)  # 开始按照ip连接
    message = f'我是服务端我开始发送消息了，is牛逼{i}'
    print('发送的时候测试' + message)
    consumer.send(message.encode('utf-8'))  # 发消息,说话(只能发送字节类型)

    feedback = consumer.recv(BUF_SIZE)  # 接收服务端发来的消息
    print(feedback.decode('utf-8'))

    consumer.close()  # 客户端关闭
    i += 1
    if i == 100:
        break
