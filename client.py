import socket
import random
import header
import pickle


# Função para criar e enviar um pacote com o número de sequência
def send_packet(sock, message, sequence_number):
    # Criar cabeçalho com o número de sequência
    header_obj = header.COOLHeader(sequence_number, sequence_number+1, "SYN", 0)
    # Adicionar checksum ao cabeçalho
    checksum = header_obj.set_checksum(message.encode())
    # Enviar cabeçalho e mensagem
    sock.send(pickle.dumps((header_obj, message.encode())))

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


sending_op = input("Modo de envio de pacotes:\n[1]-Individualmente\n[2]-Em lote\n")

if sending_op == 1:
    sequence = 0
    count = 1

    while True:
        # Send message
        message = input("Send message: ")
        
        if message:
            if message == "\\terminate":
                sock.send(message.encode())

                break

            # Envinhando caracteres separadamente
            caracteres = list(message)

            for char in caracteres:
                hd = header.COOLHeader(sequence, count ,1)
                package = f'{hd.sequence_number},{hd.ack_number},{char}'
                
                sock.send(package.encode())

                sequence += 1
                count += 1

                # Receive ACK
                ack = sock.recv(1024).decode()

                # Confirm ACK
                if ack == "ACK":
                    print("Message received by server.")
                else:
                    print("Package lost.")

elif sending_op == 2:
    sequence = 0
    count = 1

    while True:
        # Send message
        message = input("Send message: ")
        
        if message:
            if message == "\\terminate":
                sock.send(message.encode())

                break

            # Envinhando caracteres separadamente
          
            hd = header.COOLHeader(sequence, count ,1)
            package = f'{hd.sequence_number},{hd.ack_number},{message}'
            
            sock.send(package.encode())

            sequence += 1
            count += 1

            # Receive ACK
            ack = sock.recv(1024).decode()

            # Confirm ACK
            if ack == "ACK":
                print("Message received by server.")
            else:
                print("Package lost.")
else:
    print


# Close the socket
sock.close()
