import socket

ip_port = ('127.0.0.1', 9000)
BUF_SIZE = 1024
udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket.SOCK_DGRAM 这里是udp协议

udp_server_client.bind(ip_port)  # 绑定端口和地址

while True:
    msg, addr = udp_server_client.recvfrom(BUF_SIZE)  # 这里与tcp的区别是不需要建立连接，你发过来我收到拿到你的地址和端口然后发给你就可以了
    msg = msg.decode('utf-8')
    print(f'服务器收到的消息{msg}')
    print(f'要发过来的地址和端口是：{addr}')
    # send_message = '你好我收到了现在给你流媒体数据请接收:123131316546546461212121'
    send_message = input('服务器发送')
    udp_server_client.sendto(send_message.encode('utf-8'), addr)
