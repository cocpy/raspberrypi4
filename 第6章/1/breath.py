import RPi.GPIO as GPIO
import time

# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)

# 将12号引脚设置为输出模式
GPIO.setup(12, GPIO.OUT)

# 创建一个 PWM 实例，需要两个参数：
# 第一个是GPIO端口号，这里我们用12号
# 第二个是频率（Hz），频率越高LED看上去越不会闪烁，相应对CPU要求就越高，设置合适的值就可以
pwm = GPIO.PWM(12, 80)

# 启用 PWM，参数是占空比，范围：0.0 <= 占空比 >= 100.0
pwm.start(0)

try:
    while True:
        # 电流从小到大，LED由暗到亮
        for i in range(0, 101, 1):
            # 更改占空比，
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)

        # 再让电流从大到小，LED由亮变暗
        for i in range(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)

# 捕捉 Ctrl+C 强制中断的动作，以便于清理GPIO引脚
except KeyboardInterrupt:
    pass

# 停用 PWM
pwm.stop()

# 清理GPIO引脚
GPIO.cleanup()