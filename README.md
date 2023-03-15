# CPU and GPU usage, along with GPU temperature, displayed on a 2x16 LCD using Arduino and Python.

<img src="https://user-images.githubusercontent.com/112471004/225152766-0950a4d0-928e-4c85-a6bc-78db604c0307.png" alt="image" width="800px">

## Overview
This small project utilizes an Arduino UNO and a Python script to display CPU and GPU usage, as well as GPU temperature, on a 2x16 LCD. The Python script retrieves the necessary hardware information and transmits it through a COM port at 3-second intervals, while the Arduino listens to the same port, captures the data, and outputs it to the LCD. The resulting display provides a simple and informative readout of system usage and GPU temperature metrics

---

## Installation

### Python Modules
- `pyserial`: `pip install pyserial`
- `psutil`: `pip install psutil`
- `GPUtil`: `pip install GPUtil`
- `requests_html`: `pip install requests_html`


### Arduino Libraries
- `LiquidCrystal I2C` by Frank de Brabander
---

## Acknowledgements

- This video provided assistance in the process of managing communication between Arduino UNO and the Python script.


    <em>Using an Arduino with Python LESSON 10: Passing Data from Python to Arduino</em>


---
## Images and problems
- While I had initially planned to present the CPU temperature alongside the GPU temperature, it unfortunately proved to be a challenging task as psutil lacked support for this feature on non-Linux systems.
<img src="https://user-images.githubusercontent.com/112471004/225152695-935670c6-4873-4668-ac61-6383c044f9c6.png" alt="image" width="300px">


