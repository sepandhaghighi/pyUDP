import socket
import sys
UDP_IP = ''
UDP_PORT =4660
file=open("recieve_log.txt","a")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while (True):
    data=sock.recvfrom(1024)
    print(str(data[0])[2:-1])
    file.write(str(data[0])[2:-1]+"\n")
    if str(data[0])[2:-1].upper()=="EXIT":
        file.close()
        sock.close()
        break
sock.close()
file.close()
