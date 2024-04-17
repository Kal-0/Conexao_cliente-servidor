import pickle
import header
h1 = header.COOLHeader(2, 1, 10)

test1 = b"c"
exp1 = 198

payload = "Hello, World!"
payload1 = "Hello, World!"

h1.set_checksum(payload)
print(h1.checksum)

payload = "Hello World!"

print(header.vef_checksum(h1, payload1, h1.checksum))
