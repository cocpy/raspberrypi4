# 引入RPi.GPIO库
import RPi.GPIO as GPIO
import time


# BOARD编号方式
GPIO.setmode(GPIO.BOARD)

# 定义接口
out1 = 13
out2 = 11
out3 = 15
out4 = 12

# 控制标志
i = 0
positive = 0
negative = 0
y = 0

# 设置输出模式
GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)
GPIO.setup(out4, GPIO.OUT)

try:
    while True:
        GPIO.output(out1, GPIO.LOW)
        GPIO.output(out2, GPIO.LOW)
        GPIO.output(out3, GPIO.LOW)
        GPIO.output(out4, GPIO.LOW)
        x = int(input('输入一个整数（位于-400与400之间）来控制步进电机旋转：'))

        if 0 < x <= 400:
            # 顺时针方向旋转
            for y in range(x, 0, -1):
                if negative == 1:
                    if i == 7:
                        i = 0
                    else:
                        i = i + 1
                    y = y + 2
                    negative = 0
                positive = 1
                # print((x+1)-y)
                if i == 0:
                    GPIO.output(out1, GPIO.HIGH)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 1:
                    GPIO.output(out1, GPIO.HIGH)
                    GPIO.output(out2, GPIO.HIGH)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 2:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.HIGH)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 3:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.HIGH)
                    GPIO.output(out3, GPIO.HIGH)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 4:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.HIGH)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 5:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.HIGH)
                    GPIO.output(out4, GPIO.HIGH)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 6:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.HIGH)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 7:
                    GPIO.output(out1, GPIO.HIGH)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.HIGH)
                    time.sleep(0.03)
                    # time.sleep(1)
                if i == 7:
                    i = 0
                    continue
                i = i + 1

        elif -400 <= x < 0 :
            # 逆时针方向旋转
            x = x * -1
            for y in range(x, 0, -1):
                if positive == 1:
                    if i == 0:
                        i = 7
                    else:
                        i = i - 1
                    y = y + 3
                    positive = 0
                negative = 1
                # print((x+1)-y)
                if i == 0:
                    GPIO.output(out1, GPIO.HIGH)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 1:
                    GPIO.output(out1, GPIO.HIGH)
                    GPIO.output(out2, GPIO.HIGH)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 2:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.HIGH)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 3:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.HIGH)
                    GPIO.output(out3, GPIO.HIGH)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 4:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.HIGH)
                    GPIO.output(out4, GPIO.LOW)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 5:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.HIGH)
                    GPIO.output(out4, GPIO.HIGH)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 6:
                    GPIO.output(out1, GPIO.LOW)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.HIGH)
                    time.sleep(0.03)
                    # time.sleep(1)
                elif i == 7:
                    GPIO.output(out1, GPIO.HIGH)
                    GPIO.output(out2, GPIO.LOW)
                    GPIO.output(out3, GPIO.LOW)
                    GPIO.output(out4, GPIO.HIGH)
                    time.sleep(0.03)
                    # time.sleep(1)
                if i == 0:
                    i = 7
                    continue
                i = i - 1

except KeyboardInterrupt:
    # 结束进程，释放GPIO引脚
    GPIO.cleanup()
