from sense_hat import SenseHat
import time
import random

sense = SenseHat()  # 创建Sense Hat对象

# 生成随机颜色
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
sense.show_letter("C", text_colour=[r, g, b])  # 指定文本和颜色
time.sleep(1)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
sense.show_letter("O", text_colour=[r, g, b])
time.sleep(1)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
sense.show_letter("C", text_colour=[r, g, b])
time.sleep(1)

sense.show_letter("!", text_colour=[0, 0, 0], back_colour=[255, 255, 255])  # 增加背景颜色
time.sleep(1)
sense.clear()
