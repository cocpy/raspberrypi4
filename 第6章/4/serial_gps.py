import serial

SERIAL_PORT = "/dev/serial0"
running = True


# 在NMEA消息中，将按以下方式发送位置：
# DDMM.MMMMM，其中DD表示度，而MM.MMMMM表示分钟
def formatDegreesMinutes(coordinates, digits):
    """将传输的字符串转换为所需的格式"""
    
    parts = coordinates.split(".")

    if (len(parts) != 2):
        return coordinates

    if (digits > 3 or digits < 2):
        return coordinates
    
    left = parts[0]
    right = parts[1]
    degrees = str(left[:digits])
    minutes = str(right[:3])

    return degrees + "." + minutes


def getPositionData(gps):
    """从串行端口读取数据,然后解析其传输的NMEA消息"""
    data = gps.readline()
    message = data[0:6]
    if (message == "$GPRMC"):
        # GPRMC = 建议的最小特定GPS / 传送的数据
        parts = data.split(",")
        if parts[2] == 'V':
            # 接收警告
            print("GPS receiver warning")
        else:
            # 获取随GPRMC消息一起发送的位置数据
            # 在此示例中，我仅使用经度和纬度感兴趣
            longitude = formatDegreesMinutes(parts[5], 3)
            latitude = formatDegreesMinutes(parts[3], 2)
            print("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
    else:
        # 处理其他NAME消息不支持的字符串
        pass

print ("Application started!")
gps = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 0.5)

while running:
    try:
        getPositionData(gps)
    except KeyboardInterrupt:
        running = False
        gps.close()
        print("Application closed!")
    except:
        # 做一些错误处理
        print("Application error!")