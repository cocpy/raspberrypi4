import RPi.GPIO as GPIO
import time
import random
from datetime import datetime

# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)

# 设置输 出 状态的GPIO
GPIO.setup(11, GPIO.OUT)
# 设置输 入 状态的GPIO
GPIO.setup(37, GPIO.IN)

# 11号引脚输出低电平
GPIO.output(11, GPIO.LOW)
random.seed()


try:
    while True:
        # 随机休眠指定时间
        time.sleep(random.random() * 10)
        # 获取当前时间
        start = datetime.now()
        # 11号引脚输出高电平，LED灯被点亮
        GPIO.output(11, True)
        # 检测37号引脚信号是否发生变化
        while not GPIO.input(37):
            pass
        print('你的反应时间是：', (datetime.now() - start).total_seconds())
        time.sleep(2.0)
        print('下次测试即将开始!')

        # 11号引脚输出低电平
        GPIO.output(11, False)
except Exception as e:
    print(e)

# 清理占用的GPIO资源
GPIO.cleanup()