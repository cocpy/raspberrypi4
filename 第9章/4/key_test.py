import pygame
from pygame.locals import *
from sense_hat import SenseHat


pygame.init()  # 初始化
pygame.display.set_mode((640, 480))  # 设置窗口尺寸
sense = SenseHat()  # 创建一个SenseHat对象
sense.clear()  # 清空

while True:
    for event in pygame.event.get():  # 获取输入信号
        print(event)
        if event.type == QUIT:  # 退出
            print("OVER")
            break
