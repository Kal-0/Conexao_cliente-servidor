import socket

HOST = '127.0.0.1'  # Endereço IP do servidor (localhost)
PORT = 50000  # Porta usada pelo servidor

# Criação de um objeto socket com AF_INET = IPv4 e SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelece conexão com o servidor
s.connect((HOST, PORT))

# Envia os dados codificados ao servidor
s.sendall(str.encode('BOM DIA'))

# Recebe e armazena os dados do servidor. O valor 1024 especifica o tamanho máximo dos dados que podem ser recebidos de uma vez
data = s.recv(1024)

# Imprime a mensagem ecoada recebida do servidor, decodificando os dados
print('Mensagem ecoada:', data.decode())
