import RPi.GPIO as GPIO
import time


T_SensorRight = 26
T_SensorLeft = 13

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

BtnPin = 19
Gpin = 5
Rpin = 6


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
    GPIO.setwarnings(False)                                # 忽略警告
    GPIO.setmode(GPIO.BCM)                                 # 设置编号方式

    GPIO.setup(Gpin, GPIO.OUT)                             # 将绿色LED引脚模式设置为输出
    GPIO.setup(Rpin, GPIO.OUT)                             # 将红色LED引脚模式设置为输出
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 设置BtnPin的模式输入，并上拉至高电平（3.3V）
    GPIO.setup(T_SensorRight, GPIO.IN)                     # 设置为输入模式
    GPIO.setup(T_SensorLeft, GPIO.IN)

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


def loop():
    """主循环"""
    while True:
        SR = GPIO.input(T_SensorRight)                     # 右探头，检测到黑线时，接收不到信号，输出高电平
        SL = GPIO.input(T_SensorLeft)                      # 左探头，检测到黑线时，接收不到信号，输出高电平
        if SL == False and SR == False:                    # 都未检测到黑线，小车在黑线两侧
            print("t_up")
            t_up(50, 0)                                    # 前进
        elif SL == True and SR == False:                   # 左侧检测到黑线，小车偏右，需要左转
            print("Left")
            t_left(50, 0)                                  # 左转
        elif SL == False and SR == True:                   # 右侧检测到黑线，小车偏左，需要右转
            print("Right")
            t_right(50, 0)                                 # 右转
        else:
            t_stop(0)                                      # 停止


if __name__ == '__main__':
    setup()
    keyscan()
    try:
        loop()
    except KeyboardInterrupt:                               # 使用“ Ctrl + C”快捷键终止程序
        destroy()
