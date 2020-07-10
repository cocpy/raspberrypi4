from sense_hat import SenseHat

sense = SenseHat()  # 创建Sense Hat实例

while True:
    t = sense.get_temperature()  # 读取温度
    p = sense.get_pressure()  # 读取气压
    h = sense.get_humidity()  # 读取湿度

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (t, p, h)
    sense.show_message(msg, scroll_speed=0.05)  # 在LED上显示出获取的参数