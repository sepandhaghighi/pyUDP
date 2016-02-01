import os
import subprocess
cur_direction=os.getcwd()
if __name__=="__main__":
    subprocess.Popen("py "+cur_direction+"/"+"send.py")
    subprocess.Popen("py "+cur_direction+"\\"+"recv.py")

