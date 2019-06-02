# Python client
import socket

s = socket.socket()

port = 9500
# connect to server
s.connect(('127.0.0.1', port))

# send message to server
message = b"Hello"
s.send(message)

# display response
print(s.recv(1024))
s.close()
