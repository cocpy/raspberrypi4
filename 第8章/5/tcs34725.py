import time

import board
import busio

import adafruit_tcs34725

# 初始化I2C对象
I2C = busio.I2C(board.SCL, board.SDA)

# 创建一个tcs34725对象
tcs34725 = adafruit_tcs34725.TCS34725(I2C)


# 打印读取到的范围
def tcs34725_detect():
    while True:
        # 读取传感器的颜色、色温和照度
        color = tcs34725.color_rgb_bytes
        temp = tcs34725.color_temperature
        lux = tcs34725.lux
        print('颜色: {0}, {1}, {2}'.format(*color))  # RGB格式
        print('色温: {0}K'.format(temp))
        print('照度: {0}'.format(lux))
        time.sleep(1)


if __name__ == '__main__':
    try:
        tcs34725_detect()
    except KeyboardInterrupt:
        print("程序结束！")
