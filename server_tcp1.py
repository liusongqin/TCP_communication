import socket
import threading

class Server:
    def __init__(self, host = '', port = 55506):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        self.clients = []
            
    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                for client in self.clients:
                    client.sendall(message)
                print(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print('Connected with {str(address)}')
            self.clients.append(client)
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

server = Server()
server.receive()
