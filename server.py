import socket
import pickle
import packet

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set origin
LOCALHOST = "127.0.0.1"
IP = "127.0.0.1"
PORT = 5000

sock.bind((IP, PORT))

# Listen for connections
sock.listen(1)

while True:
    print("Server is listening...\n")

    # Accept connection
    conn, addr = sock.accept()

    # Receive SYN
    p_syn = pickle.loads(conn.recv(1024))
    print(p_syn.header.flags)

    # Send SYN-ACK
    p_synack = packet.Packet(packet.COOLHeader(0, 0, "SYN-ACK", 0), "")
    conn.send(pickle.dumps(p_synack))

    #Recieve ACK
    p_ack = pickle.loads(conn.recv(1024))
    print(p_ack.header.flags)
    
    # Confirm ACK
    if p_ack.header.flags == "ACK":
        print(f"Connection established with: {addr}.\n")
        

        num_ack = 0

        while True:
            try:
                # Receive message
                message = conn.recv(1024).decode()
                
            except:
                print("something went wrong...\n")
                break
            if message == "\\terminate":
                print("Connection terminated.\n")
                break
            if message:
                # Terminate connection

                
                msg = message.split(',')
            

                if num_ack != int(msg[0]) and num_ack == 0:
                    conn.send("NACK".encode())
                
                else:
                    num_ack = int(msg[1])

                    # print("Message received.")
                    print(f"Message: {msg}")

                    # Send ACK
                    conn.send("ACK".encode())

            elif message == 2:

    # Close the connection
conn.close()
