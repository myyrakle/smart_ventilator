import socket # socket module

my_address = '블라블라' # ip address
port = 12345 # port number
socket_address=(my_address, port) # make tuple

# create server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(socket_address)
server_socket.listen(1) #queue count

print('## Server is Running ##')

# main loop
while True:
    client_socket, addr = server_socket.accept() # block until connecting
    print('# client connected')
    data = client_socket.recv(65535) # specifies  buffer-size 
    print('# client say: '+data)
    client_socket.close()
