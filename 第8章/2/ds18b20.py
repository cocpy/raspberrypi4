from w1thermsensor import W1ThermSensor

# 传感器的序列号要根据设备修改
sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "031561d43aff")

while True:
    # 获取温度
    temperature_in_celsius = sensor.get_temperature()
    # 输出温度
    print(temperature_in_celsius)
