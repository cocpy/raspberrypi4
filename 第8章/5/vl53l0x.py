import time

import board
import busio
import adafruit_vl53l0x


# 初始化I2C对象
I2C = busio.I2C(board.SCL, board.SDA)

# 创建一个vl53l0x对象
vl53l0x = adafruit_vl53l0x.VL53L0X(I2C)

# 调整测量预算时间以更改速度和精度
# 较高的速度但不太准确
# vl53l0x.measurement_timing_budget = 20000
# 较慢的速度但更加准确
# vl53l0x.measurement_timing_budget = 200000


# 打印读取到的范围
def vl53l0x_detect():
    while True:
        print("距离: {0}mm".format(vl53l0x.range))
        time.sleep(1)


if __name__ == '__main__':
    try:
        vl53l0x_detect()
    except KeyboardInterrupt:
        print("程序结束！")
