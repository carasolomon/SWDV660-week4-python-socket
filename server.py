# Python server
import socket

s = socket.socket()
print("Socket successfully created")
# identify port
port = 9500

s.bind(('', port))
print("socket binded to %s" %(port)) 

# socket is listening for connection
s.listen(5)
print("socket is listening")
while True:
    (c, addr) = s.accept()
    # show established connection
    print('Got connection from', addr)
    data = c.recv(1024)
    print(data)
    # check if data is hello, return hi to client
    if data == b'Hello':
        message = b"Hi"
        c.send(message)
    else:    
        # reject other data, return goodbye to client
        reject = b"Goodbye"
        c.send(reject)

    c.close()