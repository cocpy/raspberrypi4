import time

import RPi.GPIO as GPIO


# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)

# 使用的GPIO引脚
gpio_pin = 16

# 将第16个引脚设置为输入模式
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop_detect():
    while True:
        # 当检测是否输出低电平信号
        if GPIO.input(gpio_pin) == 0:
            print("检测到障碍物")
        else:
            print("未检测到障碍物")
        time.sleep(1)


if __name__ == '__main__':
    try:
        loop_detect()
    except KeyboardInterrupt:
        print("程序结束！")
    finally:
        GPIO.cleanup()
