import time

import smbus


# 设置MPU6050寄存器地址
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47
Register_A = 0


# 初始化一个bus对象
bus = smbus.SMBus(1)
# bus = smbus.SMBus(0)

# MPU6050设备地址
MPU6050_Address = 0x68


def init():
    """初始化方法"""
    # 写入采样率寄存器
    bus.write_byte_data(MPU6050_Address, SMPLRT_DIV, 7)
    # 写入电源管理寄存器
    bus.write_byte_data(MPU6050_Address, PWR_MGMT_1, 1)
    # 写入配置寄存器
    bus.write_byte_data(MPU6050_Address, CONFIG, 0)
    # 写入陀螺仪配置寄存器
    bus.write_byte_data(MPU6050_Address, GYRO_CONFIG, 24)
    # 写入中断允许寄存器
    bus.write_byte_data(MPU6050_Address, INT_ENABLE, 1)


def get_value(addr):
    """从传感器读取参数"""
    # 读取加速度计和陀螺仪的16位值
    high = bus.read_byte_data(MPU6050_Address, addr)
    low = bus.read_byte_data(MPU6050_Address, addr + 1)
    # 左移位运算并按位或
    value = ((high << 8) | low)
    # 从模块获取标记值
    if value > 32768:
        value = value - 65536
    return value


def main_loop():
    """主循环，打印读取到的数据"""
    # 初始化
    init()

    # 读取加速度计原始值
    acc_x = get_value(ACCEL_XOUT_H)
    acc_y = get_value(ACCEL_YOUT_H)
    acc_z = get_value(ACCEL_ZOUT_H)

    # 读取陀螺仪原始值
    gyro_x = get_value(GYRO_XOUT_H)
    gyro_y = get_value(GYRO_YOUT_H)
    gyro_z = get_value(GYRO_ZOUT_H)

    # 转换为g
    Ax = acc_x / 16384.0
    Ay = acc_y / 16384.0
    Az = acc_z / 16384.0

    # 转换位度每秒
    Gx = gyro_x / 131.0
    Gy = gyro_y / 131.0
    Gz = gyro_z / 131.0

    # 打印读取到的数据
    print("Gx=%.2f" % Gx, u'\u00b0' + "/s", "\tGy=%.2f" % Gy, u'\u00b0' + "/s", "\tGz=%.2f" % Gz, u'\u00b0' + "/s",
          "\tAx=%.2f g" % Ax, "\tAy=%.2f g" % Ay, "\tAz=%.2f g" % Az)

    time.sleep(1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")



# from mpu6050 import mpu6050
# import time
#
# sensor = mpu6050(0x68)
#
# while True:
#     accel_data = sensor.get_accel_data()
#     gyro_data = sensor.get_gyro_data()
#     temp = sensor.get_temp()
#
#     print("Accelerometer data")
#     print("x: " + str(accel_data['x']))
#     print("y: " + str(accel_data['y']))
#     print("z: " + str(accel_data['z']))
#
#     print("Gyroscope data")
#     print("x: " + str(gyro_data['x']))
#     print("y: " + str(gyro_data['y']))
#     print("z: " + str(gyro_data['z']))
#
#     print("Temp: " + str(temp) + " C")
#     time.sleep(0.5)
