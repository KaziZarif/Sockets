import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9898

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello world!".encode('utf-8'))
print(socket.recv(1024))