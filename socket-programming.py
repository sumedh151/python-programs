from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)

s.bind(('127.0.0.1', 11111))

while True:
	data, addr = s.recvfrom(1024)
	print ("Connection from", addr)
	s.sendto(data.upper(), addr)

from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)

s.bind(('127.0.0.1', 0)) # OS chooses port

print ("using", s.getsocketname())

server = ('127.0.0.1', 11111)

s.sendto("MixedCaseString", server)

data, addr = s.recvfrom(1024)

print ("received", data, "from", addr)

s.close()

# -----------------------------------------------------------------------g

from socket import socket, AF_INET,
SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)

s.bind(('127.0.0.1', 9999))

s.listen(5) # max queued connections

while True:

sock, addr = s.accept()
# use socket sock to communicate
# with client process

# ------------------------------------------------------------------------
