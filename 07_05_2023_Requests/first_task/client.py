import socket

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect(('localhost', 1337))

print(client.recv(1024).decode('utf-8'))

while True:
    message = input('>>> ')
    client.send(message.encode('utf-8'))

    data = client.recv(1024)
    print(f'[SERVER] {data.decode("utf-8")}')





