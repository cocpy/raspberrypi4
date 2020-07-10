# 本示例读取并打印等效的二氧化碳。每2秒测量一次，TVOC测量和温度
from time import sleep
from Adafruit_CCS811 import Adafruit_CCS811

ccs = Adafruit_CCS811()

while not ccs.available():
    pass

temp = ccs.calculateTemperature()
ccs.tempOffset = temp - 25.0

while True:
    if ccs.available():
        temp = ccs.calculateTemperature()
        if not ccs.readData():
            print("CO2: ", ccs.geteCO2(), "ppm, TVOC: ", ccs.getTVOC(), " temp: ", temp)
        else:
            print("ERROR!")
            while 1:
                pass
    sleep(2)
