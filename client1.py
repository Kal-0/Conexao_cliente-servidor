import socket

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect(('localhost', 5000))

# Receive ACK
ack = sock.recv(1024).decode()

# Confirm ACK
if ack == "ACK":
    print("Connection established.\n")

# Send ACK
sock.send("ACK".encode())

while True:
    # Send message
    message = input("Send message: ")
    
    if message == "\\terminate":
        sock.send(message.encode())
        break

    sock.send(message.encode())

    # Receive ACK
    ack = sock.recv(1024).decode()

    # Confirm ACK
    if ack == "ACK":
        print("Message received by server.")

# Close the socket
sock.close()
