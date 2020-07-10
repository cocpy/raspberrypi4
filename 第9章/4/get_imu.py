import time

from sense_hat import SenseHat

sense = SenseHat()  # 创建SenseHat对象

while True:
    # 获取各轴的加速度
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    x = round(x, 0)
    y = round(y, 0)
    z = round(z, 0)

    # 获取相对于水平面倾斜的数值
    orientation = sense.get_orientation()
    p = round(orientation["pitch"], 0)
    r = round(orientation["roll"], 0)
    a = round(orientation["yaw"], 0)

    print("x=%s, y=%s, z=%s" % (x, y, z))
    print("p: %s, r: %s, y: %s" % (p, r, a))

    time.sleep(1)
