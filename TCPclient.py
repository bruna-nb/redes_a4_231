import socket

def get_input(default, message):
    user_input = input(message)
    if user_input == "":
        return default
    return user_input

host = get_input("localhost", "Host/IP [Default: localhost]: ")
port = int(get_input(8080, "Port [Default: 8080]: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

count = 0
while True:
    message = input("Message to send...: ")
    if message == "":
        break
    client_socket.send(message.encode())
    reply = client_socket.recv(1024).decode()
    print(f"[{count}] {reply} ::: {message}")
    count += 1

client_socket.close()