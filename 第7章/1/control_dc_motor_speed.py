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

# 频率
frequency = 500

# 初始占空比
duty = 0

# 创建一个频率为500的PWM对象，并向ENA输入PWM脉冲信号
pwm = GPIO.PWM(ENA, frequency)

try:
    # 以duty的初始占空比开始向ENA输入PWM脉冲信号
    pwm.start(duty)

    while True:
        # 将电机设置为正向转动
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)

        # 通过改变PWM占空比，让电机转速不断加快
        for duty in range(0, 100, 5):
            # 改变PWM占空比
            pwm.ChangeDutyCycle(duty)
            time.sleep(1)

        # 将电机设置为反向转动
        GPIO.output(IN1, True)
        GPIO.output(IN2, False)

        # 通过改变PWM占空比，让电机转速不断加快
        for duty in range(0, 100, 5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(1)
except Exception as e:
    print('An exception has happened', e)

finally:
    # 停止PWM
    pwm.stop()

    # 结束进程，释放GPIO引脚
    GPIO.cleanup()
