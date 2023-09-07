import socket
import threading


def listen_server(server_socket):
    while True:
        data = server_socket.recv(1024)
        if not data:
            return
        print(data.decode('utf-8'))


client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect(('localhost', 1339))

# printing welcome message
print(client.recv(1024).decode('utf-8'))

# listening for server
t = threading.Thread(target=listen_server, args=(client, ))
t.start()

while True:
    message = input()
    client.send(message.encode('utf-8'))

    # data = client.recv(1024)
    # print(f'[SERVER] {data.decode("utf-8")}')
