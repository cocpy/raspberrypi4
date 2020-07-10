import pygame
from pygame.locals import *
from sense_hat import SenseHat


pygame.init()  # 初始化
pygame.display.set_mode((640, 480))  # 设置窗口尺寸
sense = SenseHat()  # 创建一个SenseHat对象
sense.clear()  # 清空

# 点亮(0, 0)位置处的LED
x = 0
y = 0
sense.set_pixel(x, y, 255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            sense.set_pixel(x, y, 0, 0, 0)  # 0,0,0 为熄灭状态

            if event.key == K_DOWN and y < 7:
                y = y + 1
            elif event.key == K_UP and y > 0:
                y = y - 1
            elif event.key == K_RIGHT and x < 7:
                x = x + 1
            elif event.key == K_LEFT and x > 0:
                x = x - 1

        sense.set_pixel(x, y, 255, 255, 255)
        if event.type == QUIT:
            print("BYE")
            break
