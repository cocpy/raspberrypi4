from sense_hat import SenseHat  # 引入库
sense = SenseHat()  # 创建senseHat对象
# sense.show_message("Sense Hat")  # 显示文本
sense.show_message("Sense Hat", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])

sense.clear()
