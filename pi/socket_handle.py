import socket

class SocketHandler:
    server_socket #Socket
    ipv4_my_address #String
    port #Integer
    
    fan_controller #FanController
    
    __init__():
        socket_address=(my_address, port) #make tuple
        server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(socket_address)
        server_socket.listen(1)
    
    def start(self):
        print('## Server is Running ##')
        
        while True:
            client_socket, address = server_socket.accept()
            print('@ client connected')
            # ...
            client_socket.close()
            pass
        
        
        