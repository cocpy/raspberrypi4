from pyfirmata import Arduino, util


board = Arduino('/dev/ttyACM0')


def main_loop():
    """主循环"""
    # 获取Arduino10号引脚
    # d：表示数字信号
    # 10：表示引脚编号
    # p：表示输出PWM信号
    pin_10 = board.get_pin('d:10:p')
    while True:
        duty = int(input("请输入亮度0-100："))
        pin_10.write(duty)  # 写入数值


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
