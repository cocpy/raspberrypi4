import time

import board
import busio
import adafruit_bme280

# 初始化I2C对象
i2c = busio.I2C(board.SCL, board.SDA)

# 获得传感器数据
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# 初始化SPI对象
# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# bme_cs = digitalio.DigitalInOut(board.D10)
# bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# 设置本地的海平面压力
bme280.sea_level_pressure = 1013.25

# 循环打印数据
try:
    while True:
        print("\n温度: %0.1f C" % bme280.temperature)
        print("湿度: %0.1f %%" % bme280.humidity)
        print("压强: %0.1f hPa" % bme280.pressure)
        print("海拔：%0.2f meters" % bme280.altitude)
        time.sleep(2)
except KeyboardInterrupt:
    print("程序结束！")
