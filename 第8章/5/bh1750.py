import time

import smbus


# 默认的I2C地址
DEVICE = 0x23
ONE_TIME_HIGH_RES_MODE_1 = 0x20


# 创建一个smbus实例
bus = smbus.SMBus(1)


def loop_print():

    while True:
        # 从I2C接口读取数据
        data = bus.read_i2c_block_data(DEVICE, ONE_TIME_HIGH_RES_MODE_1)

        # 将2个字节的数据转换为十进制数的简单函数
        light_level = (data[1] + (256 * data[0])) / 1.2

        print("光照强度为 : " + format(light_level,'.2f') + " lx")
        time.sleep(0.5)


if __name__ == '__main__':
    try:
        loop_print()
    except KeyboardInterrupt:
        print("程序结束！")
