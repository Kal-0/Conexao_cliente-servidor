import socket
import pickle
import packet



def sequential_comm(conn):
    num_sqc = 0
    num_ack = 0

    # flags de simulaco
    check_flag = False
    
    while True:
        # recebendo pacotes do cliente
        pack = pickle.loads(conn.recv(1024))
        num_ack = pack.header.sequence_number
        message = pack.payload
        
        # Simulando um corrompimento do pacote
        

        if(message == "Tchecksum" and check_flag == False):
            check_flag = True
            pack.payload = "corrompido"

        # faz checksum do pacote
        if(pack.vef_checksum() == False):
            print("Erro no checksum")
            # pede pacote novamente
            p_ack = packet.Packet(packet.COOLHeader(num_sqc, num_ack, "NACK", 0), "")
            conn.send(pickle.dumps(p_ack))
            num_sqc+=1
            continue

        # encerra conexao
        if message == "\\terminate" or pack.header.flags == "FIN":
            print("Connection terminated.\n")
            break
            

        
        
        # printa mensagem recebida
        print(f"sqc_num: {num_ack}, msg: {message}")
        
        # envia ack pedindo proximo pacote
        p_ack = packet.Packet(packet.COOLHeader(num_sqc, pack.header.sequence_number+1, "ACK", 0), "")
        conn.send(pickle.dumps(p_ack))

        # printa ack enviado
        print(f"Ssqc_num: {p_ack.header.sequence_number}, Sack_num: {p_ack.header.ack_number}")
        print("========================")
        
        num_sqc += 1







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

        sequential_flag = False
        batch_flag = False

        # recebendo tipo de comunicacao
        pack = pickle.loads(conn.recv(1024))
        print(pack.header.flags)
        
        if pack.header.flags == "SEQ":
            sequential_flag = True
            batch_flag = False

        elif pack.header.flags == "PAR":
            batch_flag = True
            sequential_flag = False

        


        

        num_sqc = 0
        num_ack = 0



        try:
             
            if sequential_flag:
                sequential_comm(conn) 
            else:

                while True:
                    
                    # recebendo pacotes do cliente
                    pack = pickle.loads(conn.recv(1024))
                    num_ack = pack.header.sequence_number
                    message = pack.payload

                    
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
            


   