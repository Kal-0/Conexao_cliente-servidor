import pickle

class COOLHeader:
    def __init__(self, sequence_number:int, ack_number:int, window_size:int):
        self.sequence_number = sequence_number
        self.ack_number = ack_number
        self.flags = None
        self.window_size = window_size
        self.header_length = None
        self.checksum = None
    
    def set_checksum(self, payload):
        self.checksum = calculate_checksum(pickle.dumps(
            [self.sequence_number, self.ack_number, self.flags, self.window_size, self.header_length, payload]
        ))
        return self.checksum




def calculate_checksum(packet):
    checksum = 0

    #soma de bytes para checksum
    for i in range(0, len(packet), 1):
        checksum += packet[i]


    return checksum

def vef_checksum(header, payload, checksum):
    lista_packet = [header.sequence_number, header.ack_number, header.flags, header.window_size, header.header_length, payload]
    vef = calculate_checksum(pickle.dumps(lista_packet))

    if vef == checksum:
        return True

    return False


#TODO
    #Soma de verificação; Feito
    #Temporizador;
    #Número de sequência; Feito
    #Reconhecimento;
    #Reconhecimento negativo;
    #Ver se o ACK ta certo
    #Janela, paralelismo.
