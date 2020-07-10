import smbus
import time
import random


bus = smbus.SMBus(1)


def main_loop():
    """主循环，发送数据"""
    while True:
        value = random.randint(0, 255)  # 产生随机数，范围0－255
        print('value; ', value)
        bus.write_byte(0x08, value)  # 向地址8发送数据
        time.sleep(0.5)  # 延时0.5秒


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
