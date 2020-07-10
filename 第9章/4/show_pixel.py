from sense_hat import SenseHat

sense = SenseHat()

sense.set_pixel(0, 2, [0, 0, 255])  # 第1（0+1）列第3（2+1）行的LED设置为蓝色
sense.set_pixel(7, 4, [255, 0, 0])  # 第8（7+1）列第5（4+1）行的LED设置为红色
