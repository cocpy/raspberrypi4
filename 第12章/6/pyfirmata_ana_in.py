import time

from pyfirmata import Arduino, util


board = Arduino('/dev/ttyACM0')

# 获取Arduino0号引脚
# d：表示数字信号
# 0：表示引脚编号
# i：表示输入
pin_0 = board.get_pin('a:0:i')

ite = util.Iterator(board)  # 管理读数
ite.start()

pin_0.enable_reporting()  # 启用报告功能

def main_loop():
    """主循环"""

    while True:
        value = pin_0.read()  # 读取数据
        if value != None:
            voltage = value * 5.0
            print("读数为：", voltage)
        time.sleep(1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
