# Showing CPU/GPU usage and GPU temperature on 2x16LCD.
![image](https://user-images.githubusercontent.com/112471004/225152766-0950a4d0-928e-4c85-a6bc-78db604c0307.png)

Basically how it works:
  - Python fetches the hardware information and then sends the wanted information trough a COM port(every 3 seconds).
  - Arduino listens to the same COM port and catches the information and then prints it on the lcd.
  
This video provided assistance in the process of managing communication between Arduino UNO and the Python script.
[![Video Name](https://img.youtube.com/vi/dbZZlq1_M4o/maxresdefault.jpg)](https://www.youtube.com/watch?v=dbZZlq1_M4o)



<img src="https://user-images.githubusercontent.com/112471004/225152695-935670c6-4873-4668-ac61-6383c044f9c6.png" alt="image" width="300px">
