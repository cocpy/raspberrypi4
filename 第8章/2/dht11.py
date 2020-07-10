import time
import board
import adafruit_dht


# 设置传感器类型，可以为DHT11、DHT22或AM2302
# 设置连接的GPIO引脚board.D4
dht_device = adafruit_dht.DHT11(board.D4)

while True:
    try:
        # 将值打印到串行端口
        tem_c = dht_device.temperature
        tem_f = tem_c * (9 / 5) + 32
        hum = dht_device.humidity
        # 打印读取到的信息
        print(
            "温度: {:.1f} °F / {:.1f} °C    湿度: {}% ".format(tem_f, tem_c, hum)
        )

    except RuntimeError as error:
        # 打印出错误信息
        print(error.args[0])

    time.sleep(2.0)
