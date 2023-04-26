import socket

# Definindo as configurações do servidor
host = input("Host/IP [Default: localhost]: ") or "localhost"
port = int(input("Port [Default: 8080]: ") or 8080)

# Criando um socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associando o socket ao endereço do servidor
sock.bind((host, port))

print("<<< Socket created >>>")
print("<<< Socket bind complete >>>")

# Loop principal para receber mensagens
while True:
    # Recebendo mensagem do cliente
    message, address = sock.recvfrom(1024)

    # Exibindo mensagem na tela
    print(f"Message [{address[0]}:{address[1]}]: {message.decode()}")

    # Enviando resposta para o cliente
    response = str(message.decode())
    sock.sendto(response.encode(), address)