import time

import RPi.GPIO as GPIO


# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)

# 指定Trig和Echo的引脚编号
trig = 16
echo = 18
i = 0

# 设置输出模式
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

# 校准
GPIO.output(trig, False)
print("正在校准传感器")

time.sleep(2)


def get_distance():
    """返回到障碍物的距离"""
    # 发射10微秒的信号
    GPIO.output(trig, True)
    time.sleep(0.00001)

    # 结束发射
    GPIO.output(trig, False)

    # 检测回声信号
    while GPIO.input(echo) == 0:
        # 开始时间
        start_time = time.time()

    while GPIO.input(echo) == 1:
        # 结束时间
        end_time = time.time()

    # 持续时间
    duration = end_time - start_time

    # 计算距离，单位为cm
    distance = duration * 17150

    return distance


if __name__ == '__main__':
    try:
        while True:
            distance = get_distance()
            print("距离是：", distance)
            time.sleep(2)
    except KeyboardInterrupt:
        print("程序结束！")

    finally:
        GPIO.cleanup()
