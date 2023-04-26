import socket

# Definindo as configurações do servidor
host = input("Host/IP [Default: localhost]: ") or "localhost"
port = int(input("Port [Default: 8080]: ") or 8080)

# Criando um socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Loop principal para enviar mensagens
while True:
    # Aguardando entrada do usuário
    message = input("Message to send...: ")

    # Verificando se o usuário deseja encerrar o cliente
    if message.lower() == "exit":
        break

    # Enviando mensagem ao servidor
    sock.sendto(message.encode(), (host, port))

    # Aguardando resposta do servidor
    response, addr = sock.recvfrom(1024)

    # Exibindo resposta do servidor
    print(f"Server reply......: [{response.decode()}] OK ::: {message}")

# Encerrando a conexão
sock.close()