import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9898

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
# communication_socket, address = server.accept()
# print("Conntected to {address}")

while True:
    communication_socket, address = server.accept()
    print(f"Conntected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is : {message}")
    communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")