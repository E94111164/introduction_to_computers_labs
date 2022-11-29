import socket, threading
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.caddress = clientAddress
    def run(self):
        print ('Connected by', self.caddress)
        print('Waiting for connection...')
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        # msg = ''
        while True:
            data = self.csocket.recv(2048)
            if len(data)==0:
                self.csocket.close()
                break
            msg = data.decode()
            print(str(self.caddress) + ': '+msg)
            self.csocket.send(bytes(msg,'UTF-8'))
        print(str(self.caddress) , "closed connection")
LOCALHOST = '10.3.141.1'
PORT = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started at: " + LOCALHOST + ':' + str(PORT))
print("Waiting for connection...")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
