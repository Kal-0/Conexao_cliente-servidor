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
    
        
        check_flag = False
        ack_flag = False
        sequential_flag = False
        batch_flag = False
        print_flag = False

        while True:
            num_sqc = 0
       
            try:
                while True:

                    pack = pickle.loads(conn.recv(1024))
                    message = pack.payload
                    
                    if message == "\\terminate":
                        print("Connection terminated.\n")
                        break


                    if message == "seq_send":
                        print("Sequencial")
                        sequential_flag = True
                        batch_flag = False
                    elif message == "batch_send":
                        print("Em lote")
                        batch_flag = True
                        sequential_flag = False


                    if sequential_flag:
                        
                        # Simulando um corrompimento do pacote
                        if(message == "Tchecksum" and check_flag == False):
                            check_flag = True
                            pack.payload = "corrompido"

                        if(pack.vef_checksum() == False):
                            print("Erro no checksum")
                            p_ack = packet.Packet(packet.COOLHeader(num_sqc, pack.header.sequence_number, "ACK", 0), "")
                            conn.send(pickle.dumps(p_ack))
                            break

                        
                        
                        if message == "Tnotreceived" and ack_flag == False:
                            ack_flag = True
                            print(f"Pacote nao recebido {pack.header.sequence_number}")
                            print("=====")
                            p_nack = packet.Packet(packet.COOLHeader(num_sqc, pack.header.sequence_number, "NACK", 0), "")
                            conn.send(pickle.dumps(p_nack))
                            num_sqc += 1
                        else:
                            p_ack = packet.Packet(packet.COOLHeader(num_sqc, pack.header.sequence_number+1, "ACK", 0), "")
                            conn.send(pickle.dumps(p_ack))
                            num_sqc += 1
                            print(message)
                            print("=====")



                    elif batch_flag:
                        # Simulando um corrompimento do pacote
                        if(message[0] == "Tchecksum0" and check_flag == False):
                            check_flag = True
                            pack.payload = "corrompido"

                        if(pack.vef_checksum() == False):
                            print("Erro no checksum")
                            p_ack = packet.Packet(packet.COOLHeader(num_sqc, pack.header.sequence_number, "ACK", 0), "")
                            conn.send(pickle.dumps(p_ack))
                            break

                        
                        
                        if message[0] == "Tnotreceived0" and ack_flag == False:
                            ack_flag = True
                            print("Lote nao recebido")
                            print("=====")
                            p_nack = packet.Packet(packet.COOLHeader(num_sqc, pack.header.sequence_number, "NACK", 0), "")
                            conn.send(pickle.dumps(p_nack))
                        else:
                            p_ack = packet.Packet(packet.COOLHeader(num_sqc, pack.header.sequence_number+1, "ACK", 0), "")
                            conn.send(pickle.dumps(p_ack))
                            num_sqc += 1
                            print(message)
                            print("=====")
                            
                  


            except:
                print("something went wrong...\n")
                break


   