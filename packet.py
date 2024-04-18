import pickle


def calculate_checksum(data):
    checksum = 0

    #soma de bytes para checksum
    for i in range(0, len(data), 1):
        checksum += data[i]

    return checksum


   


class COOLHeader:
    def __init__(self, sequence_number:int, ack_number:int, flags:str, window_size:int):
        self.sequence_number = sequence_number
        self.ack_number = ack_number
        self.flags = flags
        self.window_size = window_size
        self.header_length = None
        self.checksum = None


class Packet:
    def __init__(self, header:COOLHeader, payload):
        self.header = header
        self.payload = payload

    def get_checksum(self):
        packet_list = [self.header.sequence_number, self.header.ack_number, self.header.flags, self.header.window_size, self.header.header_length, self.payload]
        return calculate_checksum(pickle.dumps(packet_list))

    def set_checksum(self):
        self.header.checksum = self.get_checksum()
        return self.header.checksum


    def vef_checksum(self):

        if self.header.checksum == self.get_checksum():
            return True

        return False










#TODO
        #Soma de verificação; Feito
        #Temporizador;
        #Número de sequência;
        #Reconhecimento;
        #Reconhecimento negativo;
        #Janela, paralelismo.