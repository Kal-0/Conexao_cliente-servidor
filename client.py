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


if p_ack.header.flags == "ACK":
    print(f"Connection established with: '{d_ip}', {d_port}.\n")
# Menu do usuario
user_option = input("Operacao a ser realizada:\n[1]-Envio individual de pacotes\n[2]-Envio em lote de pacotes\n[3]Simular perda de pacotes\
                    \n[4]Simular erro de integridade(Checksum)\n")




# Mandando individualmente
if user_option == '1':
    sequence = 0
    ack_number = 1


    while True:

        timerThread = threading.Thread(target = timerCallback)
        timerThread.start()

        # Send message
        message = input("Send message: ")
        
        if message:
            if message == "\\terminate":
                sock.send(message.encode())

                break

            # Envinhando caracteres separadamente
            caracteres = list(message)

            for char in caracteres:

                pack = packet.Packet(packet.COOLHeader(sequence, ack_number, "", 1), char)

                sock.send(pickle.dumps(pack))
 
                sequence += 1
                ack_number += 1

                # Receive ACK
                ack = sock.recv(1024).decode()

                # Confirm ACK
                if ack == "ACK":
                    print("Message received by server.")
                else:
                    print("Package lost.")
            timerThread.cancel()



#Mandando em lote
elif user_option == '2':
    sequence = 0
    ack_number = 1

    while True:
        timerThread = threading.Thread(target = timerCallback)
        timerThread.start()
        # Send message
        message = input("Send message: ")
        
        if message:
            if message == "\\terminate":
                sock.send(message.encode())

                break
            
            last_ack = len(message)

            hd_batch = header.COOLHeader(sequence, last_ack ,1)
            package_batch = f'{hd_batch.sequence_number},{hd_batch.ack_number},{message}'
            
            sock.send(package_batch.encode())

            # Receive ACK
            ack = sock.recv(1024).decode()

            # Confirm ACK
            if ack == "ACK":
                print("Package batch received by server.")
            # else:
            #     print("Package batch lost.")


# Simulando erro 
elif user_option == '3':
   print("a")

else:
    print("Opcao invalida")


# Close the socket
sock.close()