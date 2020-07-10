import time

# sudo pip3 install adafruit-blinka
# sudo pip3 install adafruit-circuitpython-pca9685
# sudo pip3 install adafruit-circuitpython-servokit
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
from adafruit_motor import servo


i2c_bus = busio.I2C(SCL, SDA)
pwm = PCA9685(i2c_bus)                                     # 使用默认地址初始化PWM设备

pwm.frequency = 50                                         # 将频率设置为50 Hz

servo_12 = servo.Servo(pwm.channels[12])                   # 指定第12通道的舵机（从0开始）
servo_15 = servo.Servo(pwm.channels[15])                   # 指定第15通道的舵机


print('Moving servo on channel 0, press Ctrl-C to quit...')
servo_12.angle = 90
servo_15.angle = 90
while True:
    # 伺服电机转动最小角度和最大角度
    servo_12.angle = 0
    servo_15.angle = 0
    time.sleep(1)
    servo_12.angle = 0
    servo_15.angle = 180
    time.sleep(1)
