import socket

ip_port = ('127.0.0.1', 9000)
BUF_SIZE = 1024  # 收发消息的尺寸
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 目的生成socket对象
server.bind(ip_port)  # 绑定ip和端口
server.listen(5)  # 手机待机
print('服务启动开始接收消息了')
conn, addr = server.accept()  # 阻塞的等待一旦有连接进来就会拿到对应的数据
# print(conn)
# print(addr)
print('接到来自%s ip' % addr[0])

msg = conn.recv(BUF_SIZE)  # 听消息,听话
print(msg.decode('utf-8'), type(msg))  # 接收到的消息

conn.send(msg.upper())  # 服务端发消息给客户端

conn.close()  # 关闭与客户端的连接

server.close()  # 服务端关闭
