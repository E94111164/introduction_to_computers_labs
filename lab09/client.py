import socket

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Connected to: ' + str(HOST) +':8000')

while True:
    outdata = input('Send: ')
    s.send(outdata.encode())
    
    indata = s.recv(1024)
    if outdata == 'EXIT': # connection closed
        s.close()
        print('Closed connection.')
        break
    print('Echo: ' + indata.decode())