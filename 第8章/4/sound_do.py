import time

import RPi.GPIO as GPIO


# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)

# 定义传感器连接的GPIO引脚
sound = 16

# 指定16号引脚模式为输入模式
# 默认拉高到高电平，低电平表示OUT口有输出
GPIO.setup(sound, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # 检测声音传感器模块是否输出低电平
        if GPIO.input(sound) == 0:
            print("检测到声音！")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("停止检测声音！")

finally:
    GPIO.cleanup()
