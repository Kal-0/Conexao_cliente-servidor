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
        
        

        while True:
            num_sqc = 0
            num_ack = 0
            try:
                # Receive message
                while True:

                    pack = pickle.loads(conn.recv(1024))
                    message = pack.payload

                    print(message)
                    print("=====")

                    if message:
                    # Terminate connection
                        if message == "\\terminate":
                            print("Connection terminated.\n")
                            break

                    
                    #para simular erro de ack errado apague +1
                    p_ack = packet.Packet(packet.COOLHeader(num_sqc, pack.header.sequence_number+1, "ACK", 0), "")
                    conn.send(pickle.dumps(p_ack))

            except:
                print("something went wrong...\n")
                break

            if message:
                # Terminate connection
                if message == "\\terminate":
                    print("Connection terminated.\n")
                    break

            num_sqc += 1
            num_ack += 1

                
            #print("///")

    # Close the connection
    conn.close()
