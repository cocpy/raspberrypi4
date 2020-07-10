import RPi.GPIO as GPIO

# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)

# 将第11个引脚设置为输出模式
GPIO.setup(11, GPIO.OUT)

# 在第11个引脚上创建一个频率为1HZ的PWM实例
p = GPIO.PWM(11, 1)

try:
    # 启用PWM
    p.start(50)
    while True:
        pass
except KeyboardInterrupt:
    # 停止PWM
    p.stop()
finally:
    # 释放引脚
    GPIO.cleanup()
