import socket
import threading
import time

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_socket.bind(('localhost', 1339))
server_socket.listen(1)


def listen_client(client_socket, address):
    global client_sockets
    client_sockets.append(client_socket)

    print(f'Client connected! {address}')
    greeting = f'Welcome in chat!\n[{time.strftime("%H:%M:%S")}]'
    client_socket.send(greeting.encode('utf-8'))

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        data = f'[{address}] {data.decode("utf-8")}'
        print(data)

        for guest_socket in client_sockets:
            if guest_socket is not client_socket:
                guest_socket.send(data.encode('utf-8'))

    client_sockets.remove(client_socket)
    print(f'Client [{address}] disconnected!')


client_sockets = []
while True:
    print(f'Connected clients: {len(client_sockets)}')
    print('Listening for connection...')
    client_socket, address = server_socket.accept()

    t = threading.Thread(target=listen_client, args=(client_socket, address))
    t.start()
