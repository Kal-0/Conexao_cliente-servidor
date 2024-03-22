import socket

def server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind(('localhost', 12345))
    
    # Listen for incoming connections
    server_socket.listen(5)
    
    print("Server is listening...")
    
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        
        try:
            print(f"Connection from {client_address}")
            
            # Receive data from the client
            data = client_socket.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
                
                # Send a response back to the client
                client_socket.sendall(b"Server received your message")
                
            else:
                print("No more data from client")
                break
            
        finally:
            # Close the connection
            print("close-server")
            client_socket.close()

if __name__ == "__main__":
    server()
