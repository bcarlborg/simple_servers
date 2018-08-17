from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)

# I don't know what this function does yet? Still confusing to me?
# what is bind used for exactly
server_socket.bind(('', server_port))
print("This server socket is bound and ready to go!")

while true:
    message, client_addr = server_socket.recvfrom(2048)
    modified_message = message.upper()
    serverSocket.sendto(modified_message, client_addr)
