from socket import *

server_name = '10.0.2.15'
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)
message = input("Please enter a lower case string: ")

client_socket.sendto(message.encode("utf-8"), (server_name, server_port))
print("did we get here?")
modified_message, server_addr = client_socket.recvfrom(2048)
print(modified_message)

client_socket.close()
