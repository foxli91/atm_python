import socket

ip_addr_port = ('127.0.0.1', 9000)
BUF_SIZE = 1024
udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket.SOCK_DGRAM 这里是udp协议

while True:
    msg = input('>>: ').strip()
    if not msg: continue
    # 这里发送消息
    print('发送之前')
    udp_server_client.sendto(msg.encode('utf-8'), ip_addr_port)
    print('发送之后')
    # 这里接收消息
    print('接收之前')
    # 这里是返回的信息和对于的服务器地址端口
    # 注意这里是阻塞的，客户端一旦启动之后执行到这里会等待服务器发送消息过来会死等
    back_msg, addr = udp_server_client.recvfrom(BUF_SIZE)
    print(back_msg.decode('utf-8'), addr)
    print('接收之后')
