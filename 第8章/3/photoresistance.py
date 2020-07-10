import time

import RPi.GPIO as GPIO


# 指定编号规则为BCM
GPIO.setmode(GPIO.BCM)

# 将引脚设置为输入模式
GPIO.setup(23, GPIO.IN)


def loop_print():
    while True:

        if GPIO.input(23):
            pass
        else:
            print("检测到的光线亮度已超过阀值！")
        time.sleep(1)


if __name__ == '__main__':
    try:
        loop_print()
    except KeyboardInterrupt:
        print("程序结束！")
    finally:
        GPIO.cleanup()
