import socket
import random
import pickle
import packet
import time
import threading

def handle_timeout(sequence, ack_number, char):

    sequence = 0
    ack_number = 1

    pack = packet.Packet(packet.COOLHeader(sequence, ack_number, "", 1), char)

    sock.send(pickle.dumps(pack))


def timerCallback():
    timeout = 25
    
    startTime = time.time()

    while True:
        if time.time() - start_time > timeout:
            handle_timeout(sequence, ack_number, char)
            print("Timeout. Pacote reenviado.")

            start_time = time.time()




# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Set origin
LOCALHOST = "127.0.0.1"
ip = "127.0.0.2"


# Set a random port
port = random.randint(5000, 6000)
sock.bind((ip, port))


# Set destiny
d_ip = "127.0.0.1"
d_port = 5000


# Connect to the server
sock.connect((d_ip, d_port))


# Send SYN
p_syn = packet.Packet(packet.COOLHeader(0, 0, "SYN", 0), "")
sock.send(pickle.dumps(p_syn))

# Receive SYN-ACK
p_synack = pickle.loads(sock.recv(1024))
print(p_synack.header.flags)


# Send ACK
p_ack = packet.Packet(packet.COOLHeader(0, 0, "ACK", 0), "")
sock.send(pickle.dumps(p_ack))


# conexao estabelecida
print(f"Connection established with: '{d_ip}', {d_port}.\n")

#inicio do envio de pacotes

# Menu do usuario
user_option = input("Operacao a ser realizada:\n[1]-Envio individual de pacotes\n[2]-Envio em lote de pacotes\n")


# Mandando individualmente
if user_option == '1':
    sqc_num = 0
    ack_num = 0

    # envia tipo de comunicacao para servidor
    pack = packet.Packet(packet.COOLHeader(sqc_num, ack_num, "SEQ", 0), "")
    sock.send(pickle.dumps(pack))

    while True:
        # Send message
        message = input("Send message: ")
        
        if message:
            # encerra conexao
            if message == "\\terminate":
                pack = packet.Packet(packet.COOLHeader(sqc_num, 0, "FIN", 0), "")
                sock.send(pickle.dumps(pack))
                break

            # envia pacotes
            while True:
                pack = packet.Packet(packet.COOLHeader(sqc_num, 0, "", 1), message)
                sock.send(pickle.dumps(pack))

                print(f"Ssqc_num: {pack.header.sequence_number}, Smsg: {pack.payload}")


                # recebe ack para proximo pacote
                p_ack = pickle.loads(sock.recv(1024))
                print(f"sqc_num: {p_ack.header.sequence_number}, ack_num: {p_ack.header.ack_number}")
                print("========================")
                if p_ack.header.flags == "ACK" and p_ack.header.ack_number == sqc_num+1:
                    print(f"ACK[{p_ack.header.ack_number}] >>>>")
                    # sai do loop e cria proximo pacote
                    break
                elif p_ack.header.flags == "NACK":
                    print(f"NACK[{p_ack.header.ack_number}] XXX")


            sqc_num += 1
            




#Mandando em lote
elif user_option == '2':
    sqc_num = 0
    ack_num = 0
    
    pack = packet.Packet(packet.COOLHeader(sqc_num, ack_num, "", 10), "batch_send")
    sock.send(pickle.dumps(pack))

    while True:
        # Send message
        message = input("Send message: ")
        
        if message:
            if message == "\\terminate":
                pack = packet.Packet(packet.COOLHeader(sqc_num, ack_num, "FIN", 10), "")
                sock.send(pickle.dumps(pack))
                break

            # Envinhando pacotes em rajada
            while True:
                my_array = []

                qnt_package = input("Quantidade de pacotes no lote: ")
                
                for i in range(int(qnt_package)):
                    my_array.append(f'{message}{sqc_num}')
                    sqc_num+=1

                pack = packet.Packet(packet.COOLHeader(sqc_num, ack_num, "", 10), my_array)
                sock.send(pickle.dumps(pack))

                

                # Confirmar o recebimento do pacote
                p_ack = pickle.loads(sock.recv(1024))
                if p_ack.header.flags == "ACK":
                    
                    ack_num += 1
                    break

                elif p_ack.header.flags == "NACK":
                    ack_num += 1
                    break


            




else:
    print("Opcao invalida")


# Close the socket
sock.close()
