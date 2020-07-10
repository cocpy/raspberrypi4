import RPi.GPIO as GPIO
import time

DIN = 12
CS = 16
CLK = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)

buffer0 = ['00011100', '00100010', '00100010', '00100010', '00100010', '00100010', '00100010', '00011100']  # 0
buffer1 = ['00011000', '00001000', '00001000', '00001000', '00001000', '00001000', '00001000', '00011100']  # 1
buffer2 = ['00011100', '00100010', '00100010', '00000100', '00001000', '00010000', '00100000', '00111110']  # 2
buffer3 = ['00011100', '00100010', '00000010', '00001100', '00000010', '00000010', '00100010', '00011100']  # 3
buffer4 = ['00000100', '00001100', '00010100', '00100100', '01000100', '01111110', '00000100', '00000100']  # 4
buffer5 = ['00111110', '00100000', '00100000', '00111100', '00000010', '00000010', '00100010', '00011100']  # 5
buffer6 = ['00011100', '00100010', '00100000', '00111100', '00100010', '00100010', '00100010', '00011100']  # 6
buffer7 = ['00111110', '00100100', '00000100', '00001000', '00001000', '00001000', '00001000', '00001000']  # 7
buffer8 = ['00011100', '00100010', '00100010', '00011100', '00100010', '00100010', '00100010', '00011100']  # 8
buffer9 = ['00011100', '00100010', '00100010', '00100010', '00011110', '00000010', '00100010', '00011100']  # 9
buffer = [buffer0, buffer1, buffer2, buffer3, buffer4, buffer5, buffer6, buffer7, buffer8, buffer9]


def send(byteData):
    for bit in range(0, 8):
        if (byteData & 0x80):
            GPIO.output(DIN, True)
        else:
            GPIO.output(DIN, False)
        byteData = byteData << 1
        GPIO.output(CLK, True)
        GPIO.output(CLK, False)


def writeWord(addr, num):
    GPIO.output(CS, True)
    GPIO.output(CS, False)
    GPIO.output(CLK, False)
    send(addr)
    send(num)
    GPIO.output(CS, True)


def draw(index):
    for i in range(0, 8):
        writeWord(i + 1, int(buffer[index][i], 2))


def initData():
    writeWord(0x09, 0x00)
    writeWord(0x0a, 0x03)
    writeWord(0x0b, 0x07)
    writeWord(0x0c, 0x01)
    writeWord(0xff, 0x00)


try:
    initData()
    for i in range(0, 10):
        draw(i)
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()