'''Módulo que contém a classe Client_Server que é responsável por criar um servidor e um cliente que se comunicam entre si'''
import socket

class ClientServer:
    def __init__(self, host:str='localhost', port:int=12345):
        
        self.HOST = host
        self.PORT = port

    def server(self):
        '''
        Método que cria um servidor que fica esperando por conexões de clientes,
        quando um cliente se conecta, o servidor recebe uma mensagem do cliente
        e envia uma mensagem de confirmação de recebimento da mensagem
        '''
        # Criando um Socket TCP/IP
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Ligando o socket à porta
        server_socket.bind((self.HOST, self.PORT))

        # Escutando por conexões
        server_socket.listen(5)

        print("HOST - waiting for a connection")

        while True:
            # Esperando por conexões
            client_socket, client_address = server_socket.accept()

            try:
                print(f"HOST - connection from {client_address}")

                while True:
                    # Recebendo a mensagem do cliente 
                    data = client_socket.recv(1024)

                    if not data:
                        break

                    print(f"HOST - received: {data.decode()}")

                    # Mandando mensagem de confirmação do recebimento da mensagem do cliente
                    client_socket.sendall(b"PONG")


            finally:
                # Fechando a conexão do servidor
                print("HOST - connection close")
                client_socket.close()
                break

    def client(self, message):
        '''
        Método que cria um cliente que se conecta a um servidor e envia uma mensagem
        '''
        # Criando um Socket TCP/IP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectando o socket ao servidor
        client_socket.connect((self.HOST, self.PORT))

        try:
            # Mandando a mensagem para o servidor

            print(f"CLIENT - sending: {message}")
            client_socket.sendall(message.encode())

            # Recebendo a resposta do servidor
            data = client_socket.recv(1024)
            print(f"CLIENT - received: {data.decode()}")


        finally:
            # Fechando a conexão do cliente
            print("CLIENT - connection close")
            client_socket.close()
