import socket

def client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the server
    client_socket.connect(('localhost', 12345))
    
    try:
        # Send data to the server
        message = "Hello, server!"
        print(f"Sending: {message}")
        client_socket.sendall(message.encode())
        
        # Receive response from the server
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
        client_socket.close()
        
    finally:
        # Close the connection
        print("finally")

if __name__ == "__main__":
    client()
