import time
import math

import RPi.GPIO as GPIO
import smbus


# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)

# 设置地址
address = 0x48
cmd=0x40

# 创建一个smbus实例
bus=smbus.SMBus(1)


def loop_print():
    """遍历打印数据"""
    while True:
        # 读取数据
        value = bus.read_byte_data(address, cmd)

        # 计算电压
        voltage = value / 255.0 * 3.3

        # 计算电阻
        Rt = 10 * voltage / (3.3 - voltage)

        # 获取当前开尔文温度
        temp_K = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0)

        # 转化为摄氏度
        temp_C = temp_K - 273.15

        print('当前温度为：', temp_C)
        time.sleep(0.01)


if __name__ == '__main__':
    try:
        loop_print()
    except KeyboardInterrupt:
        print("程序结束！")
    finally:
        GPIO.cleanup()
