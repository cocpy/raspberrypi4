import time
import board
import busio
import adafruit_veml6075


# 创建一个I2C对象
I2C = busio.I2C(board.SCL, board.SDA)

# 获取veml对象
veml = adafruit_veml6075.VEML6075(I2C, integration_time=100)


def veml_detect():
    while True:
        print("检测到的读数是：", veml.uv_index)
        time.sleep(1)


if __name__ == '__main__':
    try:
        veml_detect()
    except KeyboardInterrupt:
        print("程序结束！")
