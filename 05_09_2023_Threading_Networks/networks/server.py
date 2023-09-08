# socket
# protocol

import socket

# IPv4
# 192.168.0.1
# 127.0.0.1
# 8.8.8.8

# SOCK_STREAM = TCP

# TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.0.107', 1234))
server.listen(2)

print('Waiting for connection...')
client, client_address = server.accept()

print(f'Client connected! {client_address}')
client.send(b'Hello, client!')
# receive
data = client.recv(1024)
print(f'Message from client: {data.decode("utf-8")}')
client.close()
print('Server completed!')
