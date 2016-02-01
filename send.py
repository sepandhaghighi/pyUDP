import socket
import os
import subprocess
current_direct=os.getcwd()
socket.socket.accept
my_ip=socket.gethostbyname(socket.gethostname())
file=open("chat_log.txt","a")
print("Your Device IP : " + my_ip)
ip=input("Please Enter Target Ip: ")
port=int(input("Please Enter Port : "))
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#value=subprocess.Popen("py "+current_direct+"\\recv.py")
#print(value)
while(True):
    message=input("You : ")
    file.write("You : "+message+"\n")
    if message.upper()=="EXIT":
        sock.sendto("Terminate".encode("utf-8"),(ip,port))
        file.close()
        break
    message=my_ip+":"+message
    sock.sendto(message.encode("utf-8"),(ip,port))
