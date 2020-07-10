import RPi.GPIO as GPIO
import time


# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)
# 将第8个引脚设置为输出模式
GPIO.setup(8, GPIO.OUT)


def buzz(pitch, duration):
    """发出声音"""
    period = 1.0/pitch
    delay = period / 2
    cycles=int(duration*pitch)
    for i in range(cycles):
        # 输出低电平
        GPIO.output(8, GPIO.LOW)
        time.sleep(delay)
        # 输出高电平
        GPIO.output(8, GPIO.HIGH)
        time.sleep(delay)


while(True):
    # 输入频率
    pitch_s = input("Enter Pitch (200 to 2000,do262,rui294,mi330)")
    pitch= float(pitch_s)
    # 持续时间
    duration_s= input("Enter Duration (Seconds)")
    duration=float(duration_s)
    # 发出声音
    buzz(pitch, duration)