import pickle
import packet

h1 = packet.COOLHeader(2, 1, "ack", 10)
payload = "Hello, World!"

p1 = packet.Packet(h1, payload)


payload1 = "Hello World!"


print(p1.header.checksum)
print(p1.get_checksum())
p1.set_checksum()
print(p1.header.checksum)


#simular corrupçãoVVV
#p1.payload = payload1
#print(p1.get_checksum())


print(p1.vef_checksum())




