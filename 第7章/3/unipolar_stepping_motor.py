import RPi.GPIO as GPIO
import time


# BOARD编号方式
GPIO.setmode(GPIO.BOARD)

# 定义接口
coil_A_1_pin = 7
coil_A_2_pin = 11
coil_B_1_pin = 16
coil_B_2_pin = 18

# 设置输出模式
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)


def forward(delay, steps):
    """向前转动"""
    for i in range(0, steps):
        set_step(1, 0, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 0, 1)
        time.sleep(delay)
        set_step(1, 0, 0, 1)
        time.sleep(delay)


def backwards(delay, steps):
    """向后转动"""
    for i in range(0, steps):
        set_step(1, 0, 0, 1)
        time.sleep(delay)
        set_step(0, 1, 0, 1)
        time.sleep(delay)
        set_step(0, 1, 1, 0)
        time.sleep(delay)
        set_step(1, 0, 1, 0)
        time.sleep(delay)


def set_step(w1, w2, w3, w4):
    """启动电机"""
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)


try:
    while True:
        # 输入每步之间的间隔（单位为毫秒）
        delay = input("Delay between steps (milliseconds)?")
        # 输入向前转动步数
        steps = input("How many steps forward?")
        forward(int(delay) / 1000.0, int(steps))
        # 输入向后转动步数
        steps = input("How many steps backwards? ")
        backwards(int(delay) / 1000.0, int(steps))

except Exception as e:
    print('An exception has happened', e)

finally:
    # 结束进程，释放GPIO引脚
    GPIO.cleanup()
