import RPi.GPIO as GPIO
import time

DIN = 12
CS = 16
CLK = 18

# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)
# 设置输出模式
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)

buffer = ['00000000', '01100110', '11111111', '11111111', '11111111', '01111110', '00111100', '00011000']
# buffer = [0x00,0x66,0xff,0xff,0xff,0x7e,0x3c,0x18]


# 传递数据
def send(byteData):
    for bit in range(0, 8):
        if (byteData & 0x80):
            GPIO.output(DIN, True)
        else:
            GPIO.output(DIN, False)
        byteData = byteData << 1
        GPIO.output(CLK, True)
        GPIO.output(CLK, False)


# 写入数据
def writeWord(addr, num):
    GPIO.output(CS, True)
    GPIO.output(CS, False)
    GPIO.output(CLK, False)
    send(addr)
    send(num)
    GPIO.output(CS, True)


def draw():
    for i in range(0, 8):
        print("%d %d" % (i, int(buffer[i], 2)))
        writeWord(i + 1, int(buffer[i], 2))


# 初始化数据
def initData():
    writeWord(0x09, 0x00)
    writeWord(0x0a, 0x03)
    writeWord(0x0b, 0x07)
    writeWord(0x0c, 0x01)
    writeWord(0xff, 0x00)


try:
    initData()
    draw()
except KeyboardInterrupt:
    pass

# 释放资源
GPIO.cleanup()
