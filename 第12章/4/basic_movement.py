import RPi.GPIO as GPIO
import time


PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24
                                               # 运动方向


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


def setup():
    """初始化"""
    GPIO.setwarnings(False)                    # 忽略警告
    GPIO.setmode(GPIO.BCM)                     # 设置编号方式
    GPIO.setup(AIN2, GPIO.OUT)                 # 设置为输出模式
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(PWMA, GPIO.OUT)

    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)

    global L_Motor                             # 设置全局变量
    L_Motor = GPIO.PWM(PWMA, 100)              # 初始化一个频率为100Hz的PWM实例
    L_Motor.start(0)                           # 启用PWM

    global R_Motor
    R_Motor = GPIO.PWM(PWMB, 100)
    R_Motor.start(0)


def loop():
    """主循环"""
    while True:
        t_up(50, 3)
        t_down(50, 3)
        t_left(50, 3)
        t_right(50, 3)
        t_stop(3)


def destroy():
    """释放资源"""
    L_Motor.stop()                             # 停止PWM实例
    R_Motor.stop()
    GPIO.cleanup()                             # 释放引脚


if __name__ == '__main__':                     # 程序入口
    setup()
    try:
        loop()
    except KeyboardInterrupt:                  # 使用“ Ctrl + C”快捷键终止程序
        destroy()
