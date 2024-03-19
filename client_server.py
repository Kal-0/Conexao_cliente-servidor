import socket, multiprocessing



# Definindo a porta que vai ser utilizada para a comunicação
PORT = 12345 
HOST = "localhost"


def server():
    # Criando um SOcket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Linkando o socket ao HOST e a porta que será utilizada
    server_socket.bind((HOST, PORT)) 
    
    # Listen for incoming connections
    server_socket.listen(5)
    
    print("HOST - listening...")
    
    while True:
        # Aceitando a conexão requisitada pelo cliente
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
    

            
            
def client(message):
    # Criando um Socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conectando o socket ao servidor
    client_socket.connect((HOST, PORT))
    
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
        
        
        
        
if __name__ == "__main__":

    message = input()

    # Criando 2 threads, uma para o cliente e a outra para o servidor
    process_server = multiprocessing.Process(target=server)
    process_client = multiprocessing.Process(target=client)

    process_server = multiprocessing.Process(target=server)
    process_client = multiprocessing.Process(target=client, args=(message,))

    process_server.start()
    process_client.start()
    
    process_server.join()
    process_client.join()
    