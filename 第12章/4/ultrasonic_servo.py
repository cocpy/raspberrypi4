import time

import RPi.GPIO as GPIO
# sudo pip3 install adafruit-blinka
# sudo pip3 install adafruit-circuitpython-pca9685
# sudo pip3 install adafruit-circuitpython-servokit
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
from adafruit_motor import servo

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

BtnPin= 19
Gpin = 5
Rpin = 6

TRIG = 20
ECHO = 21

i2c_bus = busio.I2C(SCL, SDA)
pwm = PCA9685(i2c_bus)                                     # 使用默认地址初始化PWM设备

pwm.frequency = 50                                         # 将频率设置为50 Hz

servo_0 = servo.Servo(pwm.channels[0])


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
    L_Motor.stop()                                         # 停止PWM实例
    R_Motor.stop()
    GPIO.cleanup()                                         # 释放引脚


def distance():
    """计算距离"""
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    time1 = time.time()                                    # 开始时间
    while GPIO.input(ECHO) == 1:                           # 监测接收引脚电平变化
        pass
    time2 = time.time()                                    # 结束时间
    during = time2 - time1                                 # 获得时间差
    return during * 340 / 2 * 100                          # 返回计算的距离


def front_detection():
    """检测前方到障碍物的距离"""
    servo_0.angle = 90                                     # 舵机转到90°
    time.sleep(0.5)
    dis_f = distance()
    return dis_f


def left_detection():
    """检测左侧到障碍物的距离"""
    servo_0.angle = 180                                    # 如果舵机装反，此处可改为0
    time.sleep(0.5)
    dis_l = distance()                                     # 检测到障碍物的距离
    return dis_l


def right_detection():
    """检测右侧到障碍物的距离"""
    servo_0.angle = 0                                      # 如果舵机装反，此处可改为180
    time.sleep(0.5)
    dis_r = distance()                                     # 检测到障碍物的距离
    return dis_r


def loop():
    """主循环"""
    while True:
        dis1 = front_detection()                            # 检测前方到障碍物的距离
        if dis1 < 60:                                       # 自动避障
            t_stop(0.2)
            t_down(50, 0.5)                                 # 后退0.5秒
            print("t_down")
            t_stop(0.2)
            dis2 = left_detection()                         # 检测左侧到障碍物的距离
            dis3 = right_detection()                        # 检测右侧到障碍物的距离
            if dis2 < 60 and dis3 < 60:
                t_left(50, 1)
                print("t_left")
            elif dis2 > dis3:                               # 左侧距离大，向左转
                t_left(50, 0.3)
                print("t_left")
                t_stop(0.1)
            else:                                           # 右侧距离大，向右转
                t_right(50, 0.3)
                print("t_right")
                t_stop(0.1)
        else:
            t_up(60, 0)                                     # 前进
            print("t_up")
        print(dis1, 'cm')


if __name__ == "__main__":                                  # 程序入口
    setup()
    keyscan()
    try:
        loop()
    except KeyboardInterrupt:                               # 使用“ Ctrl + C”快捷键终止程序
        destroy()
