import RPi.GPIO as GPIO
import time


# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)
# 将第8个引脚设置为输出模式
GPIO.setup(8, GPIO.OUT)


def beep(seconds):

    # 根据模块高低电平触发条件调正输出信号
    GPIO.output(8, GPIO.LOW)
    time.sleep(seconds)
    GPIO.output(8, GPIO.HIGH)


def beepAction(secs, sleepsecs, times):

    for i in range(times):
        beep(secs)
        time.sleep(sleepsecs)

# （鸣叫时间，停顿间隔时间，总时长）
beepAction(0.02,0.2,15)

# 结束进程，释放GPIO引脚
GPIO.cleanup()
