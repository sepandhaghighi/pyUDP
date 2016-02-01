import socket
import sys
UDP_IP = ''
UDP_PORT =4660

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind((UDP_IP,UDP_PORT))
while (True):
    data=sock.recvfrom(1024)
    print(str(data[0])[2:-1])
sock.close()
