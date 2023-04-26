import socket

def get_input(default, message):
    user_input = input(message)
    if user_input == "":
        return default
    return user_input

host = get_input("localhost", "Host/IP [Default: localhost]: ")
port = int(get_input(8080, "Port [Default: 8080]: "))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print("<<< Socket created >>>")
print("<<< Socket bind complete >>>")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"<<< Accepted connection from {client_address[0]}:{client_address[1]} >>>")
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Message [{client_address[0]}:{client_address[1]}]: {message}")
        ms = "OK"
        client_socket.send(ms.encode())
    client_socket.close()