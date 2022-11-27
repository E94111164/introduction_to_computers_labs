import socket, threading
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
    def run(self):
        print ('Connected by', clientAddress)
        print('Waiting for connection...')
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='EXIT':
              break
            print (str(clientAddress) + ': '+msg)
            self.csocket.send(bytes(msg,'UTF-8'))
        print (str(clientAddress) , "closed connection")
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