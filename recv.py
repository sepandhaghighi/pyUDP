import socket
import sys
import datetime
UDP_IP = ''
UDP_PORT =4660
file=open("recieve_log.txt","a")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while (True):
    now_time=str(datetime.datetime.now())
    data=sock.recvfrom(1024)
    print(str(data[0])[2:-1]+"\t\t"+now_time)
    file.write(str(data[0])[2:-1]+"\t\t"+now_time+"\n")
    if str(data[0])[2:-1].upper()=="EXIT":
        file.close()
        sock.close()
        break
sock.close()
file.close()
