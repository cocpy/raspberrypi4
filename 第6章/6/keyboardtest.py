import RPi.GPIO as GPIO


# 省略部分设置代码

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if (GPIO.input(C1) == 1):
        print(characters[0])
    if (GPIO.input(C2) == 1):
        print(characters[1])
    if (GPIO.input(C3) == 1):
        print(characters[2])
    if (GPIO.input(C4) == 1):
        print(characters[3])
    GPIO.output(line, GPIO.LOW)


try:
    while True:
        readLine(L1, ["1", "2", "4", "A"])
        readLine(L2, ["4", "5", "6", "B"])
        readLine(L3, ["7", "8", "9", "C"])
        readLine(L4, ["*", "0", "#", "D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nApplication stopped!")
