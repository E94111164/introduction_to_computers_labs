import socket

HOST = '10.3.141.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Connected to: ' + str(HOST) +':8000')

while True:
    outdata = input('Send: ')

    if outdata == 'EXIT': # connection closed
        print('Closed connection.')
        break
    s.send(outdata.encode())
    indata = s.recv(1024)
    print('Echo: ' + indata.decode())
s.close()
