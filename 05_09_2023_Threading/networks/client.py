import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Connecting...')
client.connect(('127.0.0.1', 1234))
print('Connected!')

print('Getting data from server...')
data_from_server = client.recv(1024)
print(f'Message from server: {data_from_server.decode("utf-8")}')
client.send(b"Hey server, how are you?")
client.close()
