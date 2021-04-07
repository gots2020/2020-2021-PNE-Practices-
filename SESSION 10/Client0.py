import socket
import termcolor
from termcolor import colored

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up.")
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running?")

    def __str__(self):
        return "Connection to server at " + self.ip + ", " + "PORT : " + str(self.port)

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To Server: ", msg)
        s.send(msg.encode())
        response = s.recv(2048).decode("utf-8")
        s.close()
        return "From server: " + response


    def debug_talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To Server: ", termcolor.colored(msg, 'blue'))
        s.send(msg.encode())
        response = s.recv(2048).decode("utf-8")
        print("From server: ", end="")
        print(termcolor.colored(response, 'green'))
        s.close()
        return "From server: " + response