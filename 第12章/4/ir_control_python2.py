# -*- coding: UTF-8 -*-
#!/usr/bin/python
import time

import pylirc
import RPi.GPIO as GPIO


PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

BtnPin = 19
Gpin = 5
Rpin = 6

blocking = 0


def t_up(speed,t_time):
    """前进"""
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, False)
    GPIO.output(AIN1, True)                     # 左前

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, False)
    GPIO.output(BIN1, True)                     # 右前
    time.sleep(t_time)


def t_down(speed,t_time):
    """后退"""
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)                     # 左后
    GPIO.output(AIN1, False)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)                     # 右后
    GPIO.output(BIN1, False)
    time.sleep(t_time)


def t_left(speed,t_time):
    """原地左转"""
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)                     # 左后
    GPIO.output(AIN1, False)

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, False)
    GPIO.output(BIN1, True)                     # 右前
    time.sleep(t_time)


def t_right(speed,t_time):
    """原地右转"""
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, False)
    GPIO.output(AIN1, True)                     # 左前

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)                     # 右后
    GPIO.output(BIN1, False)
    time.sleep(t_time)


def t_stop(t_time):
    """停止"""
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2, False)
    GPIO.output(AIN1, False)

    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN2, False)
    GPIO.output(BIN1, False)
    time.sleep(t_time)


def keyscan():
    """按键开关"""
    while not GPIO.input(BtnPin):                          # 监听BtnPin是否为低电平
        pass
    while GPIO.input(BtnPin):                              # 监听BtnPin是否为高电平，低->高，按键按下，程序往下执行
        time.sleep(0.01)
        val = GPIO.input(BtnPin)
        if val:
            GPIO.output(Rpin, 1)
            while not GPIO.input(BtnPin):
                GPIO.output(Rpin, 0)
        else:
            GPIO.output(Rpin, 0)


def setup():
    """初始化"""
    GPIO.setwarnings(False)                                # 忽略警告
    GPIO.setmode(GPIO.BCM)                                 # 设置编号方式

    GPIO.setup(Rpin, GPIO.OUT)                             # 将红色LED引脚模式设置为输出
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置BtnPin的模式输入，并上拉至高电平（4.3V）

    GPIO.setup(AIN2, GPIO.OUT)                             # 设置为输出模式
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(PWMA, GPIO.OUT)

    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)

    global L_Motor                                         # 设置全局变量
    L_Motor = GPIO.PWM(PWMA, 100)                          # 初始化一个频率为100Hz的PWM实例
    L_Motor.start(0)                                       # 启用PWM

    global R_Motor
    R_Motor = GPIO.PWM(PWMB, 100)
    R_Motor.start(0)


def destroy():
    """释放资源"""
    pylirc.exit()
    L_Motor.stop()                                         # 停止PWM实例
    R_Motor.stop()
    GPIO.cleanup()                                         # 释放引脚


def ir(config):
    """键值匹配查询"""
    if config == 'KEY_CHANNEL':
        t_up(50,0)
        # print 't_up'
    elif config == 'KEY_NEXT':
        t_stop(0)
        # print 't_stop'
    elif config == 'KEY_PREVIOUS':
        t_left(50,0)
        # print 't_left'
    elif config == 'KEY_PLAYPAUSE':
        t_right(50,0)
        # print 't_right'
    elif config == 'KEY_VOLUMEUP':
        t_down(50,0)
        # print 't_down'


def loop():
    """主循环"""
    while True:
        s = pylirc.nextcode(1)
        while s:                                            # 读取红外键值
            for (code) in s:
                # print 'Command: ', code["config"]
                ir(code["config"])                          # 查询文件
            if not blocking:
                s = pylirc.nextcode(1)
            else:
                s = []


if __name__ == "__main__":                                  # 程序入口
    setup()
    keyscan()
    pylirc.init("pylirc", "./conf", blocking)               # 初始化配置文件
    try:
        loop()
    except KeyboardInterrupt:                               # 使用“ Ctrl + C”快捷键终止程序
        destroy()
