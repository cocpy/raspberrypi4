from time import sleep

from pyfirmata import Arduino, util


board = Arduino('/dev/ttyACM0')


def main_loop():
    """主循环"""
    # 获取Arduino13号引脚
    # d：表示数字信号
    # 13：表示引脚编号
    # o：表示输出
    pin_13 = board.get_pin('d:13:o')
    while True:
        pin_13.write(0)  # 写入低电平
        sleep(1)
        pin_13.write(1)  # 写入高电平
        sleep(1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")

