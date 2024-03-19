class Header:
    def __init__(self, id, source, destination, length):
        self.id = id
        self.source = source
        self.destination = destination
        self.length = length

    
class Packet:
    def __init__(self, header, payload):
        self.header = header
        self.payload = payload
