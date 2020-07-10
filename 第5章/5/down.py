import RPi.GPIO as GPIO
import time

# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)

# 设置物理引脚11负责输出电压
GPIO.setup(11, GPIO.OUT)

# 关闭警告
GPIO.setwarnings(False)

# 设置输入引脚
channel = 15

# 设置GPIO输入模式, 使用GPIO内置的下拉电阻, 即开关断开情况下输入为LOW
GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# 检测LOW -> HIGH的变化
GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=200)


def on_switch_pressed():
    """开关闭合的处理方法,点亮LED灯0.1秒"""
    # 11号引脚输出高电平
    GPIO.output(11, GPIO.HIGH)
    # 持续一秒
    time.sleep(0.1)
    # 11号引脚输出低电平
    GPIO.output(11, GPIO.LOW)


try:
    while True:
        # 如果检测到电平RISING, 说明开关闭合
        if GPIO.event_detected(channel):
            on_switch_pressed()
        # 10毫秒的检测间隔
        time.sleep(0.01)
except Exception as e:
    print(e)

# 清理占用的GPIO资源
GPIO.cleanup()