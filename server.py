import socket
import header
import pickle

# # Função para processar um pacote recebido
# def process_packet(conn, packet):
#     # Extrair cabeçalho e mensagem do pacote
#     header_obj, message = pickle.loads(packet)

#     # Verificar checksum
#     if header_obj.checksum == header.calculate_checksum(message):

#         # Verificar se é o próximo número de sequência esperado
#         if header_obj.sequence_number == expected_sequence_number:
#             # Enviar ACK
#             ack_header = header.COOLHeader(0, header_obj.sequence_number + 1, "ACK", 0)
#             conn.send(pickle.dumps((ack_header, b"")))
            
#             # Incrementar número de sequência esperado
#             expected_sequence_number += 1
#             print(f"Message received: {message.decode()}")

#         else:
#             # Pacote fora de ordem, enviar NACK para retransmissão
#             nack_header = header.COOLHeader(0, expected_sequence_number, "NACK", 0)
#             conn.send(pickle.dumps((nack_header, b"")))
#     else:
#         # Pacote corrompido, enviar NACK para retransmissão
#         nack_header = header.COOLHeader(0, expected_sequence_number, "NACK", 0)
#         conn.send(pickle.dumps((nack_header, b"")))

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

    # Send ACK
    conn.send("ACK".encode())

    #Recieve ACK
    ack = conn.recv(1024).decode()

    # Confirm ACK
    if ack == "ACK":
        print(f"Connection established with: {addr}.\n")
        num_ack = 0

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
                
                msg = message.split(',')
                
                # print(f'sequencial: {msg[0]}')
                # print(f'num ack: {msg[1]}')
                # print(f'num arck servidor:{num_ack}')

                if num_ack != int(msg[0]) and num_ack != 0:
                    conn.send("NACK".encode())
                
                else:
                    num_ack = int(msg[1])

                    # print("Message received.")
                    print(f"Message: {msg}")

                    # Send ACK
                    conn.send("ACK".encode())
            #print("///")

    # Close the connection
    conn.close()
