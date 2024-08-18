def main(blver):
    import os

    version = "0.1"
    blver = blver
    path = os.getcwd()
    nickname = "Admin"

    os.system("cls")
    print(f"Exchange {version}")
    print("输入\"return\"以回到主界面\n")

    while True:
        try:
            cmd = input("Exchange-cmd> ")
            cs = cmd.split(" ")
            if cs[0] == "return":
                break

            elif cs[0] == "command":
                print("connect: 连接其他计算机服务端")
                print("create: 以此电脑为主机创建连接")
                print("nickname: 更改昵称")

            elif cs[0] == "nickname":
                nickname = cs[1]
                print("更改成功\n")

            elif cs[0] == "connect":
                import socket, threading
                # 客户端想要发消息和收消息同时进行,需要使用多线程达到并发效果

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = socket.gethostname()
                s.connect((host, 9090))

                def receive():
                    while True:
                        data = s.recv(1024).decode('utf-8')
                        if data != '':
                            print(data)

                def send_msg():
                    while True:
                        msg = input(':')
                        if msg == 'exit':
                            s.close()
                            break
                        s.send(bytes(msg.encode('utf-8')))

                t1 = threading.Thread(target=receive, daemon=True)
                t1.start()

                send_msg()


            elif cs[0] == "create":
                import socket
                import queue
                import threading
                import time
                # author : ali
                # date : 2021年8月17日
                serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = socket.gethostname()
                print(socket.gethostbyname(host))
                serversocket.bind((host, 9090))
                serversocket.listen(5)
                # 存放已连接的对象
                clients = []
                # 存放公共消息的容器
                public_message = dict()

                # 接收新的对象
                def init():
                    while True:
                        client, addr = serversocket.accept()  # 阻塞线程
                        if client in clients:
                            print('老用户')
                        else:
                            print('新的用户加入:', end='')
                            print(client.getpeername()[0])
                            client.send(bytes('欢迎来到聊天室(匿名)!'.encode('utf-8')))
                            clients.append(client)
                            r = threading.Thread(target=receive_msg, args=(client,))
                            r.start()

                # 接收消息
                def receive_msg(client):
                    while True:
                        time.sleep(1)
                        try:
                            if client in clients:
                                data = client.recv(1024).decode('utf-8')
                                if data != '':
                                    print(data)
                                    public_message[client] = queue.Queue()
                                    public_message[client].put(data)
                                else:
                                    if client in clients:
                                        print("用户优雅的退出了")
                                        clients.remove(client)

                        except BaseException as error:

                            print('用户强制中断了一个连接')
                            # print('错误:',error)
                            if client in clients:
                                clients.remove(client)

                # 转发消息(非/阻塞)
                def broadcast():
                    while True:
                        if len(clients) > 1:
                            public_message_clone = [i for i in public_message]  # 解决字典迭代中操作报错的问题
                            for client in clients:
                                for i in public_message_clone:
                                    if i != client and public_message[i].empty() == False:
                                        data = public_message[i].get_nowait()  # 注意
                                        if data != '':
                                            client.send(bytes(data.encode('utf-8')))
                                            print('服务器转发了消息')

                t1 = threading.Thread(target=init)
                t2 = threading.Thread(target=broadcast)

                t1.start()
                t2.start()

                # 主线程监听在线人数
                while True:
                    print("当前在线人数为:%d" % (len(clients)))
                    time.sleep(5)




            else:
                pass

        except IndexError:
            print("缺少必要的参数")

