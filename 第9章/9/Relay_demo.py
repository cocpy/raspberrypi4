import RPi.GPIO as GPIO
import time

Relay = [5, 6, 13, 16, 19, 20, 21, 26]  # 各通道继电器使用的引脚

GPIO.setmode(GPIO.BCM)  # 编号模式
GPIO.setwarnings(False)  # 忽略警告

for i in range(0, 8):
    GPIO.setup(Relay[i], GPIO.OUT)
    GPIO.output(Relay[i], GPIO.HIGH)

try:
    while True:
        for i in range(8):
            GPIO.output(Relay[i], GPIO.LOW)
            time.sleep(0.5)
        for i in range(8):
            GPIO.output(Relay[i], GPIO.HIGH)
            time.sleep(0.5)
except:
    GPIO.cleanup()  # 释放资源
