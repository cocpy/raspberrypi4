import RPi.GPIO as GPIO
import time


Buzzer = 11

CL = [0, 131, 147, 165, 175, 196, 211, 248]  # 低音C频率

CM = [0, 262, 294, 330, 350, 393, 441, 495]  # 中央C频率

CH = [0, 525, 589, 661, 700, 786, 882, 990]  # 高音C频率

song_1 = [CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6],  # 第一首曲谱
          CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
          CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
          CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]]

beat_1 = [1, 1, 3, 1, 1, 3, 1, 1,  # 第一首曲子的节拍, 1 表示 1/8 拍
          1, 1, 1, 1, 1, 1, 3, 1,
          1, 3, 1, 1, 1, 1, 1, 1,
          1, 2, 1, 1, 1, 1, 1, 1,
          1, 1, 3]

song_2 = [CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1],  # 第二首曲谱
          CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
          CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
          CM[3], CM[2], CL[5], CL[7], CM[2], CM[1]]

beat_2 = [1, 1, 2, 2, 1, 1, 2, 2,  # 第二首曲子的节拍, 1 表示 1/8 拍
          1, 1, 2, 2, 1, 1, 3, 1,
          1, 2, 2, 1, 1, 2, 2, 1,
          1, 2, 2, 1, 1, 3]


def setup():
    """初始化"""
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)                 # 设置编号方式
    GPIO.setup(Buzzer, GPIO.OUT)             # 设置为输出模式
    global Buzz                              # 分配一个全局变量来替换GPIO.PWM
    Buzz = GPIO.PWM(Buzzer, 440)             # 初始化一个频率为440Hz的PWM对象
    Buzz.start(50)                           # 以50%的占空比启动蜂鸣器的引脚


def loop():
    """主循环"""
    while True:
        print('\n    Playing song 1...')
        for i in range(1, len(song_1)):      # 播放第一首曲子
            Buzz.ChangeFrequency(song_1[i])  # 改变歌曲音符的频率
            time.sleep(beat_1[i] * 0.5)      # 延迟音符* 0.5s
        time.sleep(1)                        # 等待下一首歌曲

        print('\n\n    Playing song 2...')
        for i in range(1, len(song_2)):      # 播放第二首曲子
            Buzz.ChangeFrequency(song_2[i])  # 改变歌曲音符的频率
            time.sleep(beat_2[i] * 0.5)      # 延迟音符* 0.5s


def destroy():
    """释放资源"""
    Buzz.stop()                              # 停止蜂鸣器
    GPIO.output(Buzzer, 1)                   # 将蜂鸣器引脚设置为高电平
    GPIO.cleanup()                           # 释放引脚


if __name__ == '__main__':                   # 程序启动入口
    setup()
    try:
        loop()
    except KeyboardInterrupt:                # 使用“ Ctrl + C”快捷键终止程序
        destroy()
