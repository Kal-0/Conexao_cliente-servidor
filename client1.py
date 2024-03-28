import socket
import random



# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set origin
LOCALHOST = "127.0.0.1"
ip = "127.0.0.2"
# Set a random port
port = random.randint(5000, 6000)
#port = 12345

sock.bind((ip, port))

# Set destiny
d_ip = "127.0.0.1"
d_port = 5000

# Connect to the server
sock.connect((d_ip, d_port))

# Receive ACK
ack = sock.recv(1024).decode()

# Confirm ACK
if ack == "ACK":
    print(f"Connection established with: ({d_ip}, {d_port}).\n")

# Send ACK
sock.send("ACK".encode())

while True:
    # Send message
    message = input("Send message: ")
    
    if message:
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
