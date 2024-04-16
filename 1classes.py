

class COOLHeader:
    

    def __init__(self, sequence_number, ack_number, flags, window_size):
        self.sequence_number = sequence_number
        self.ack_number = ack_number
        self.flags = flags
        self.window_size = window_size
        self.header_length = None
        self.checksum = None



#TODO
        #Soma de verificação;
        #Temporizador;
        #Número de sequência;
        #Reconhecimento;
        #Reconhecimento negativo;
        #Janela, paralelismo.