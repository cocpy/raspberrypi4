# 导入RPi.GPIO库函数命名为GPIO
import RPi.GPIO as GPIO
import time

# 将GPIO编程方式设置为BOARD模式
GPIO.setmode(GPIO.BOARD)

# 设置物理引脚11负责输出电压
GPIO.setup(11, GPIO.OUT)

print('Start blinking...')
for i in range(10):
    # 11号引脚输出高电平
    GPIO.output(11, GPIO.HIGH)
    # 持续一秒
    time.sleep(1.0)
    # 11号引脚输出低电平
    GPIO.output(11, GPIO.LOW)
    time.sleep(1.0)

# 释放使用的GPIO引脚
GPIO.cleanup()

print('Finish blinking...')