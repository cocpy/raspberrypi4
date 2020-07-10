import time

import RPi.GPIO as GPIO


# 设置使用的引脚
DT = 5
SCK = 6


def init():
    """初始化方法"""
    # 忽略警告
    GPIO.setwarnings(False)
    # 设置编号方式
    GPIO.setmode(GPIO.BCM)
    # 设置为输出模式
    GPIO.setup(SCK, GPIO.OUT)


def get_count():
    """从传感器读取参数"""
    count = 0
    GPIO.setup(DT, GPIO.OUT)
    GPIO.output(DT, 1)
    GPIO.output(SCK, 0)
    GPIO.setup(DT, GPIO.IN)
    # 检测DT是否有高电平
    while GPIO.input(DT) == 1:
        continue
    for i in range(24):
        GPIO.output(SCK, 1)
        count = count << 1
        GPIO.output(SCK, 0)
        time.sleep(0.001)
        if GPIO.input(DT) == 0:
            count = count + 1
    GPIO.output(SCK, 1)
    # 清除第24位
    count = count ^ 0x800000
    GPIO.output(SCK, 0)
    return count


def main_loop():
    """主循环，打印读取到的数据"""
    # 初始化
    init()
    while True:
        count = get_count()
        print("重量为：", count)
        time.sleep(1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
    finally:
        GPIO.cleanup()
