from time import sleep

import RPi.GPIO as GPIO


# 设置地址
GPIO_PIN = 17


def init():
    """初始化方法"""
    # 设置编号方式
    GPIO.setmode(GPIO.BCM)
    # 设置为输入模式
    GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def main_loop():
    """主循环，打印读取到的数据"""
    # 初始化
    init()
    while True:
        if not GPIO.input(GPIO_PIN):
            print("检测到磁铁")
        else:
            print("未检测到磁铁")
        sleep(1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
    finally:
        GPIO.cleanup()
