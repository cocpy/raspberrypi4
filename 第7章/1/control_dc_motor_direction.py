# 引入RPi.GPIO库函数命名为GPIO
import RPi.GPIO as GPIO
import time


# BOARD编号方式
GPIO.setmode(GPIO.BOARD)

# 定义接口
ENA = 33
IN1 = 35
IN2 = 37

# 设置输出模式
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

try:
    while True:
        # 驱动电机正向转动5秒
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
        GPIO.output(ENA, True)

        # 转动5秒
        time.sleep(5)

        # 电机停止2秒
        GPIO.output(ENA, False)
        time.sleep(2)

        # 驱动电机反向转动5秒
        GPIO.output(IN1, True)
        GPIO.output(IN2, False)
        GPIO.output(ENA, True)

        # 转动5秒
        time.sleep(5)

        # 电机停止2秒
        GPIO.output(ENA, False)
        time.sleep(2)

except Exception as e:
    print('An exception has happened', e)

finally:

    # 结束进程，释放GPIO引脚
    GPIO.cleanup()
