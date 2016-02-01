import os
import subprocess
import sys
from threading import Thread
cur_direction=os.getcwd()
def func1():
    subprocess.Popen("py "+cur_direction+"/"+"send.py")
def func2():
    subprocess.Popen("py "+cur_direction+"\\"+"recv.py")
if __name__=="__main__":
    Thread(target=func1()).start()
    Thread(target=func2()).start()
    sys.exit()

