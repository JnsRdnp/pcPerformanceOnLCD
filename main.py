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
        formatted_numGPU = f"{(gpu.load*100):.1f}".zfill(4)
        return formatted_numGPU
    return None

while True:

    formatted_numCPU = f"{(psutil.cpu_percent(interval=1)):.1f}".zfill(4) 
    sysInfo=(str(formatted_numCPU) + "%|" + str(get_gpu_info())+"%|"+str(get_gpu_temperature()))
    cmd=sysInfo
    cmd=cmd+'\r'
    arduinoData.write(cmd.encode())
    time.sleep(3)
    
