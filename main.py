import serial
import psutil
import GPUtil
import time

arduinoData = serial.Serial('com3',115200)
t=0

def get_gpu_temperature():
    gpus = GPUtil.getGPUs()
    if gpus:
        return int(gpus[0].temperature)
    return None

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        return gpu.load*100
    return None

while True:

    sysInfo=(str(psutil.cpu_percent(interval=1)) + "%| " + str(get_gpu_info())+"%| "+str(get_gpu_temperature()))
    cmd=sysInfo
    cmd=cmd+'\r'
    arduinoData.write(cmd.encode())
    time.sleep(3)
    