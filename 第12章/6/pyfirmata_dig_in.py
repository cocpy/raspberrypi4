import time

from pyfirmata import Arduino, util


board = Arduino('/dev/ttyACM0')

# 获取Arduino7号引脚
# d：表示数字信号
# 7：表示引脚编号
# i：表示输入
pin_7 = board.get_pin('d:7:i')

ite = util.Iterator(board)  # 管理读数
ite.start()

pin_7.enable_reporting()  # 启用报告功能

def main_loop():
    """主循环"""

    while True:
        state = pin_7.read()  # 读取数据
        if not state:
            print("按钮被按下")
        time.sleep(0.5)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
