import time

import RPi.GPIO as GPIO
import smbus


# 指定编号规则为BCM
GPIO.setmode(GPIO.BCM)

# 设置PCF8591地址
# 可通过 sudo i2cdetect -y 1命令查询
address = 0x48

# 创建一个smbus实例
bus = smbus.SMBus(1)


def loop_print():
    while True:
        # 发送一个控制字节到设备
        bus.write_byte(address, 0x40)

        # 从设备读取单个字节
        # 若检测到有声音，该值会变小
        vv = bus.read_byte(address)
        if vv:
            print("读取到的声音值为:", vv)
            time.sleep(0.2)


if __name__ == '__main__':
    try:
        loop_print()
    except KeyboardInterrupt:
        print("程序结束！")
    finally:
        GPIO.cleanup()
