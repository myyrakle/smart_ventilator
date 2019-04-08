from fan_control import FanController
from db_control import DBController

import socket

class SocketHandler:
    
    def __init__(self, fan, db):
        ipv4_my_address = '' #String
        port = 12345 #Integer
        self.fan_controller = fan #FanController
        self.db_controller = db 

        socket_address=(ipv4_my_address, port) #make tuple
        
        self.server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(socket_address)
        self.server_socket.listen(1)
    

    def start(self):
        print('## Server is Running ##')
        
        while True:
            client_socket, address = self.server_socket.accept()
            print('@ client connected')
            # ...
            client_socket.close()
            pass
        
        
        