import socket
import time

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_socket.bind(('localhost', 1337))
server_socket.listen(1)

while True:
    print('Listening for connection...')
    client_socket, address = server_socket.accept()
    print(f'Client connected! {address}')

    greeting = f'Welcome in chat!\n[{time.strftime("%H:%M:%S")}]'
    client_socket.send(greeting.encode('utf-8'))

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        print(f'[{address}] {data.decode("utf-8")}')
        message = input('>>> ')
        client_socket.send(message.encode('utf-8'))

    print(f'Client [{address}] disconnected!')

