# Showing CPU/GPU usage and GPU temperature on 2x16LCD.

![image](https://user-images.githubusercontent.com/112471004/225152766-0950a4d0-928e-4c85-a6bc-78db604c0307.png)

[![Build Status](https://travis-ci.org/<username>/<repo-name>.svg?branch=master)](https://travis-ci.org/<username>/<repo-name>)

## Overview
This project displays CPU/GPU usage and GPU temperature on a 2x16 LCD using an Arduino UNO and a Python script. The Python script fetches the hardware information and sends it through a COM port every 3 seconds. The Arduino listens to the same COM port, receives the information, and prints it on the LCD.

---

## Installation

### Python Modules
- `pyserial`: `pip install pyserial`
- `psutil`: `pip install psutil`
- `GPUtil`: `pip install GPUtil`

### Arduino Libraries
- `LiquidCrystal I2C` by Frank de Brabander
---

## Acknowledgements

- This video provided assistance in the process of managing communication between Arduino UNO and the Python script.

<div style="position: relative;">
    <em>Using an Arduino with Python LESSON 10: Passing Data from Python to Arduino</em>
  <img src="https://img.youtube.com/vi/dbZZlq1_M4o/maxresdefault.jpg?width=200" alt="Video Thumbnail" style="width: 100%;">
  <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; text-shadow: 0px 0px 10px black; font-weight: bold; font-size: 16px;">
  </div>
</div>

---
## Images

<img src="https://user-images.githubusercontent.com/112471004/225152695-935670c6-4873-4668-ac61-6383c044f9c6.png" alt="image" width="300px">
---
