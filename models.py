class Header:
    '''
    Define o header de um pacote
    '''
    def __init__(self, id: int, timer: bool,):
        self.id = id
        self.timer = timer

        self.unity = None # TODO: Definir unidade de medida (1 bit, 1 letra, uma palavra, etc)
        self.length = None
        self.checksum = None
    
    def set_length(self, length:int):
        '''
        Seta o tamanho do pacote em bytes
        '''
        self.length = length

    def set_checksum(self, checksum):
        '''
        Seta o checksum do pacote, responsavel por verificar a integridade do pacote
        '''
        self.checksum = checksum

    
class Packet:
    '''
    Representa um pacote e seus métodos
    '''
    def __init__(self, id:int, header:Header, payload:str):
        self.id = id
        self.header = header
        self.payload = payload
    
    '''
    TODO: Implementar métodos para:
    - serialiozar o pacote para binario para poder realizado o checksum
    - calcular o checksum do pacote
    - calcular o tamanho do pacote (payload + header)
    - setar o id do pacote

    '''
