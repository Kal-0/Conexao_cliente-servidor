import socket  # Importa o módulo

HOST = 'localhost'  # Servidor utilizado
PORT = 50000  # Porta utilizada

# Criação de um objeto 's' com AF_INET = IPv4 e SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket ao endereço e porta especificados
s.bind((HOST, PORT))

# Coloca o socket em modo de escuta
s.listen()

while True:
    print('Aguardando conexão de um cliente')
    
    # Aceita uma conexão quando ela chega, retorna uma nova tupla com o objeto de conexão e o endereço do cliente
    conn, ender = s.accept()
    print('Conectado em', ender)

    while True:
        # Recebe dados do cliente. O valor 1024 especifica o tamanho máximo dos dados que podem ser recebidos de uma vez
        data = conn.recv(1024)

        # Se não houver mais dados a serem recebidos, fecha a conexão e sai do loop
        if not data:
            print('Fechando a conexão')
            conn.close()
            break

        # Se houver dados, envia todos os dados de volta ao cliente
        conn.sendall(data)  # Envia os dados de volta ao cliente
