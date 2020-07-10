import board
import busio
import adafruit_bme280

# 初始化
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# 设置本地的海平面压力
# 该传感器只能根据压力推测出海拔高度
bme280.sea_level_pressure = 1013.25

# 打印读取到的数据
print("\n温度: %0.1f C" % bme280.temperature)
print("湿度: %0.1f %%" % bme280.humidity)
print("压强: %0.1f hPa" % bme280.pressure)
print("高度：%0.2f meters" % bme280.altitude)
