import RPi.GPIO as GPIO
import time


# 用于接收信号的引脚
pin = 36

# 设置引脚编号方式
GPIO.setmode(GPIO.BOARD)

# 将36号物理引脚设置为下拉电阻以保证精度
GPIO.setup( pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


if __name__ == '__main__':
    try:
        while True:
            is_DO = GPIO.input(pin)
            time.sleep(1)
            if is_DO:
                print('未检测到酒精')
            else:
                print('检测到酒精')
    except KeyboardInterrupt:
        print('即将退出检测')
    finally:
        # 释放引脚
        GPIO.cleanup()
