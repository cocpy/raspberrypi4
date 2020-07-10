import time

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

TRIG = 20
ECHO = 21


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

    GPIO.setup(TRIG, GPIO.OUT)                             # 输出超声波信号
    GPIO.setup(ECHO, GPIO.IN)                              # 输入超声波信号

    GPIO.setup(Gpin, GPIO.OUT)                             # 将绿色LED引脚模式设置为输出
    GPIO.setup(Rpin, GPIO.OUT)                             # 将红色LED引脚模式设置为输出
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置BtnPin的模式输入，并上拉至高电平（3.3V）

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
    L_Motor.stop()                                         # 停止PWM实例
    R_Motor.stop()
    GPIO.cleanup()                                         # 释放引脚


def distance():
    """计算距离"""
    GPIO.output(TRIG, 0)                                   # 重置
    time.sleep(0.000002)
    GPIO.output(TRIG, 1)                                   # 发射10微秒的超声波信号
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)                                   # 结束发射

    while GPIO.input(ECHO) == 0:
        pass
    time1 = time.time()                                    # 开始时间
    while GPIO.input(ECHO) == 1:                           # 监测接收引脚电平变化
        pass
    time2 = time.time()                                    # 结束时间
    during = time2 - time1                                 # 获得时间差
    return during * 340 / 2 * 100                          # 返回计算的距离


def loop():
    """主循环"""
    while True:
        dis = distance()                                   # 计算距离
        if dis < 60:
            while dis < 60:                                # 自动避障
                t_down(50, 0.5)
                t_right(50, 0.1)
                dis = distance()                           # 重新计算距离
        else:
            t_up(50, 0)                                    # 前进
        print(dis, 'cm')


if __name__ == '__main__':                                 # 程序入口
    setup()
    t_stop(.1)
    keyscan()
    try:
        loop()
    except KeyboardInterrupt:                              # 使用“ Ctrl + C”快捷键终止程序
        destroy()
