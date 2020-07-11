import RPi.GPIO as GPIO
import time

Buzzer = 8

# 定义频率
CM = [0, 330, 350, 393, 441, 495, 556, 624]

song_3 = [ CM[1],CM[1],CM[5],CM[5],CM[6],CM[6],CM[5],CM[4],CM[4],CM[3],
CM[3],CM[2],CM[2],CM[1],CM[5],CM[5],CM[4],CM[4],CM[3],CM[3],
CM[2],CM[5],CM[5],CM[4],CM[4],CM[3],CM[3],CM[2],CM[1],CM[1],
CM[5],CM[5],CM[6],CM[6],CM[5],CM[4],CM[4],CM[3],CM[3],CM[2],
CM[2],CM[1],]


beat_3 = [ 0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,
0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,]


def setup():
    """初始化"""
    # 指定编号规则为BOARD
    GPIO.setmode(GPIO.BOARD)
    # 将第8个引脚设置为输出模式
    GPIO.setup(Buzzer, GPIO.OUT)
    global Buzz
    # 在第8个引脚上创建一个频率为440HZ的PWM实例
    Buzz = GPIO.PWM(Buzzer, 440)
    # 按50%工作定额启动蜂鸣器引脚
    Buzz.start(50)


def loop():
    """循环"""
    while True:
        print('\n Playing song 4...')
        for i in range(1, len(song_3)):
            Buzz.ChangeFrequency(song_3[i])
            # 延迟一个节拍* 0.2秒的音符
            time.sleep(beat_3[i])


def destory():
    """释放资源"""
    Buzz.stop()
    GPIO.output(Buzzer, 1)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
try:
    loop()
except KeyboardInterrupt:
    destory()