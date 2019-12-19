# 多任务文件下载器客户端
import socket

if __name__ == '__main__':
    # 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 和服务端连接
    tcp_client_socket.connect(("localhost", 3356))
    # 发送下载文件的请求
    file_name = input("请输入要下载的文件名：")
    # 编码
    file_name_data = file_name.encode("utf-8")
    # 发送文件下载请求数据
    tcp_client_socket.send(file_name_data)
    # 把数据写入到文件里
    with open("/home/trr/Documents/py/client/" + file_name, "wb") as file:
        while True:
            # 循环接收文件数据
            file_data = tcp_client_socket.recv(1024)
            # 接收到数据
            if file_data:
                # 写入数据
                file.write(file_data)
            # 接收完成
            else:
                print("服务端把数据发送完成并关闭了连接")
                break
    # 在这里，客户端的套接字是要关闭的，服务端套接字因为要服务多个客户端所以不用关闭
    tcp_client_socket.close()
