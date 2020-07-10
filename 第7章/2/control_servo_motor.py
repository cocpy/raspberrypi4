# 引入RPi.GPIO库
import RPi.GPIO as GPIO


# 指定编号方式为BOARD
GPIO.setmode(GPIO.BOARD)

# 定义接口
signal = 32

# 设置输出模式
GPIO.setup(signal, GPIO.OUT)

# PWM信号频率（1000/周期T）
frequency = 50

# 创建PWM对象，并设置频率为50
pwm = GPIO.PWM(signal, frequency)


def get_duty(direction):
    """计算占空比"""
    # 如果转化为百分数，使用ChangeDutyCycle()方法时还需再转化回来
    duty = (1 / 18) * direction + 2.5
    return duty


if __name__ == '__main__':
    try:
        # 启动PWM，并设置初始占空比0
        pwm.start(0)
        while True:
            # 输入一个角度
            direction = float(input("Pleas input a direction between 0 an 180:"))
            # 应该先判断用户输入是否合法
            # 计算占空比
            duty = get_duty(direction)
            # 改变PWM占空比
            pwm.ChangeDutyCycle(duty)

    except Exception as e:
        print('An exception has happened', e)

    finally:
        # 停止PWM
        pwm.stop()

        # 结束进程，释放GPIO引脚
        GPIO.cleanup()
