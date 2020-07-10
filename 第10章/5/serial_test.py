import serial  # 引入serial包


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # 打开端口


def main_loop():
    """主循环，打印读取到的数据"""
    while True:
        str_hello = "Hello Arduino,I am  Raspberry."
        b_hello = bytes(str_hello, encoding='utf-8')  # 字符串转为字节
        ser.write(b_hello)  # 发送数据
        response = ser.readall()  # 读取返回值
        print('接收到的返回数据是：', response)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
    finally:
        ser.close()
