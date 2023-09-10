import socket
import threading
import sys

class Client:
    def __init__(self, host = 'localhost', port = 55506):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        message = "Hello, World!"

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024)
                print("message from the server")
                print(message)
            except:
                print('An error occurred!')
                self.client.close()
                break

    def write(self):
            message = raw_input("enter your message:\n")
            self.client.send(message)
            timer = threading.Timer(1.0,client.write)
            timer.start()

client = Client()

receive_thread = threading.Thread(target=client.receive)
receive_thread.start()

write_thread = threading.Thread(target=client.write)
write_thread.start()




