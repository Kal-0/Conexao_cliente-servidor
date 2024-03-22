import socket

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost
sock.bind(('localhost', 5000))

# Listen for connections
sock.listen(1)

while True:
    print("Server is listening...\n")

    # Accept connection
    conn, addr = sock.accept()
    print("Established connection.\n")

    # Send ACK
    conn.send("ACK".encode())

    #Recieve ACK
    message = conn.recv(1024).decode()

    # Confirm ACK
    if message == "ACK":

        while True:
            # Receive message
            message = conn.recv(1024).decode()

            if message == "\\terminate":
                print("Connection terminated.")
                break

            print("Message received.")
            print(f"Message: {message}")

            # Send ACK
            conn.send("ACK".encode())

    # Close the connection
    conn.close()

# Close the socket
sock.close()
