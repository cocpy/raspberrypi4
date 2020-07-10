from time import sleep

from pyfirmata import Arduino, util


board = Arduino('/dev/ttyACM0')


def main_loop():
    """主循环"""
    while True:
        board.digital[13].write(0)  # 向端口13写入低电平0   代表灭灯
        sleep(1)
        board.digital[13].write(1)  # 向端口13写入高电平1   代表亮灯
        sleep(1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
