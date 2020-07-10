import RPi.GPIO as GPIO
import time


BtnPin = 19
Gpin = 5
Rpin = 6


def setup():
    """初始化"""
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)                                   # 设置编号方式
    GPIO.setup(Gpin, GPIO.OUT)                               # 将绿色LED引脚模式设置为输出
    GPIO.setup(Rpin, GPIO.OUT)                               # 将红色LED引脚模式设置为输出
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # 设置BtnPin的模式输入，并上拉至高电平（3.3V）


def keyscan():
    """主循环"""
    while True:
        if GPIO.input(BtnPin):                               # 监听BtnPin是否为高电平
            time.sleep(0.01)                                 # 持续时间，去抖动
            if GPIO.input(BtnPin):                           # 再次监听BtnPin是否为高电平
                GPIO.output(Rpin, 1)                         # Rpin引脚输出高电平
                GPIO.output(Gpin, 0)                         # Gpin引脚输出低电平
        elif not GPIO.input(BtnPin):
            time.sleep(0.01)
            if not GPIO.input(BtnPin):
                while GPIO.input(BtnPin):
                    pass
                GPIO.output(Rpin, 0)
                GPIO.output(Gpin, 1)

    
if __name__ == '__main__':                                   # 程序入口
    setup()
    try:
        keyscan()
    except KeyboardInterrupt:                                # 使用“ Ctrl + C”快捷键终止程序
        GPIO.cleanup()                                       # 释放引脚
