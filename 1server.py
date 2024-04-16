import socket

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set origin
LOCALHOST = "127.0.0.1"
ip = "127.0.0.1"
port = 5000

sock.bind((ip, port))

# Listen for connections
sock.listen(1)

while True:
    print("Server is listening...\n")

    # Accept connection
    conn, addr = sock.accept()

    # Send ACK
    conn.send("ACK".encode())

    #Recieve ACK
    ack = conn.recv(1024).decode()

    # Confirm ACK
    if ack == "ACK":

        print(f"Connection established with: {addr}.\n")

        while True:

            try:
                # Receive message
                message = conn.recv(1024).decode()
            except:
                print("something went wrong...\n")
                break

            if message:
                # Terminate connection
                if message == "\\terminate":
                    print("Connection terminated.\n")
                    break
                
                # print("Message received.")
                print(f"Message: {message}")

                # Send ACK
                conn.send("ACK".encode())
            #print("///")

    # Close the connection
    conn.close()

# Close the socket
sock.close()
