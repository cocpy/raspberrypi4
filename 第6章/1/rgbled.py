import RPi.GPIO as GPIO
import time


# 指定引脚
R, G, B=36, 38, 40
# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)
# 设置输出模式
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

# 创建PWM实例
pwmR = GPIO.PWM(R, 60)
pwmG = GPIO.PWM(G, 60)
pwmB = GPIO.PWM(B, 60)

# 启用PWM
pwmR.start(0)
pwmG.start(0)
pwmB.start(0)


try:
    t = 1
    while True:
        # 红色灯全亮，蓝灯，绿灯全暗（红色）
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        # 绿色灯全亮，红灯，蓝灯全暗（绿色）
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        # 蓝色灯全亮，红灯，绿灯全暗（蓝色）
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

        # 红灯，绿灯全亮，蓝灯全暗（黄色）
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)

        # 红灯，蓝灯全亮，绿灯全暗（洋红色）
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

        # 绿灯，蓝灯全亮，红灯全暗（青色）
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

        # 红灯，绿灯，蓝灯全亮（白色）
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

# 捕捉 Ctrl+C 强制中断的动作，以便于清理GPIO引脚
except KeyboardInterrupt:
    pass

# 停止PWM
pwmR.stop()
pwmG.stop()
pwmB.stop()

# 释放引脚
GPIO.cleanup()
