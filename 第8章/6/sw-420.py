import time

import RPi.GPIO as GPIO


# 设置使用的引脚
GPIO_PIN = 11


def init():
    """初始化方法"""
    # 设置编号方式
    GPIO.setmode(GPIO.BOARD)
    # 设置为输出模式
    GPIO.setup(GPIO_PIN, GPIO.OUT)


def main_loop():
    """主循环，打印读取到的数据"""
    # 初始化
    init()
    while True:
        if GPIO.input(GPIO_PIN) == 1:
            print("检测到震动！")
            time.sleep(1)
        else:
            print("未检测到震动")
            time.sleep(1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
    finally:
        GPIO.cleanup()
