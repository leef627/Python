import socket
import threading
import time

# 当新的客户端连入时会调用这个方法
def on_new_connection(client_executor, addr):
    print('Accept new connection from %s:%s...' % addr)

    # 发送一个欢迎信息
    client_executor.send(bytes('Welcome'.encode('utf-8')))

    # 进入死循环，读取客户端发送的信息。
    while True:
        msg = client_executor.recv(1024).decode('utf-8')
        if(msg == 'exit'):
            print('%s:%s request close' % addr)
            break
        print('%s:%s: %s' % (addr[0], addr[1], msg))
    client_executor.close()
    print('Connection from %s:%s closed.' % addr)

# 构建Socket实例、设置端口号和监听队列大小
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('', 9999))
listener.listen(5)
print('Waiting for connect...')

# 进入死循环，等待新的客户端连入。一旦有客户端连入，就分配一个线程去做专门处理。然后自己继续等待。
while True:
    client_executor, addr = listener.accept()
    t = threading.Thread(target=on_new_connection, args=(client_executor, addr))
    t.start()