import serial
import psutil
import GPUtil
import time
import datetime
from requests_html import HTMLSession

arduinoData = serial.Serial('com3',115200)

stateHandle = 0

hwInfoPartOutOfMax = 7
maxNum = 10

#weather
s = HTMLSession()


def getTempertature(city):
    query = city
    url = f'https://www.google.com/search?q={query}+tempertature'


    r = s.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})

    #print(r.html.find('title',first = True).text)
    title_text = r.html.find('title', first=True).text

    try:
        weatheroutput = "Oulu: " + str(r.html.find('span#wob_tm', first=True).text)
    except Exception as e:
        print("An error occurred while getting the weather:", e)
        
    weatheroutput = "Weather information unavailable"
    #print(myCmd)
    return weatheroutput


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
    if stateHandle<=hwInfoPartOutOfMax:
        formatted_numCPU = f"{(psutil.cpu_percent(interval=1)):.1f}".zfill(4) 
        sysInfo=(str(formatted_numCPU) + "%|" + str(get_gpu_info())+"%|"+str(get_gpu_temperature()))
    elif stateHandle>hwInfoPartOutOfMax:
        currentTime = (datetime.datetime.now().strftime("%H:%M"))
        currentTimeStr = str(currentTime)
        sysInfo=currentTimeStr+getTempertature("Oulu")
        if stateHandle==maxNum:
            stateHandle=0

    cmd=sysInfo
    cmd=cmd+'\r'

    arduinoData.write(cmd.encode())

    stateHandle+=1
    time.sleep(3)




    
