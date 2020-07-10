try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("引入错误")


GPIO.setmode(GPIO.BOARD)
# or
GPIO.setmode(GPIO.BCM)


GPIO.setwarnings(False)


channel = 1
state = 1

# 将引脚设置为输入模式
# channel是基于您指定的编号系统（BOARD或BCM）的通道号
GPIO.setup(channel, GPIO.IN)

# 将引脚设置为输出模式
GPIO.setup(channel, GPIO.OUT)

# 为输出的引脚设置默认值
GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)


# state可以设置为0/GPIO.LOW/False或1/GPIO.HIGH/True
GPIO.output(channel, state)

# 也可使用元组
chan_list = [11,12]
# 设置所有的GPIO.LOW
GPIO.output(chan_list, GPIO.LOW)
# 组中第一个设置为高第二个设置为底
GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))


# 发现有关您的RPi的信息
GPIO.RPI_INFO

# 发现Raspberry Pi电路板版本
GPIO.RPI_INFO [ 'P1_REVISION']
GPIO.RPI_REVISION  # 已弃用

# 要发现RPi.GPIO的版本
GPIO.VERSION


GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# or
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

import time
while GPIO.input(channel) == GPIO.LOW:
    time.sleep(0.01)


# 可以检测GPIO.RISING，GPIO.FALLING或GPIO.BOTH类型的边沿
# 它们占用的CPU时间可忽略不计
channel = GPIO.wait_for_edge(channel, GPIO.RISING, timeout=5000)
if channel is None:
    print('Timeout occurred')
else:
    print('Edge detected on channel', channel)


GPIO.add_event_detect(channel, GPIO.RISING)
# 省略部分业务代码
# 下面的代码放在一个线程中循环执行
if GPIO.event_detected(channel):
    print('Button pressed')


def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')

GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)


def my_callback_one(channel):
    print('Callback one')

def my_callback_two(channel):
    print('Callback two')

GPIO.add_event_detect(channel, GPIO.RISING)
GPIO.add_event_callback(channel, my_callback_one)
GPIO.add_event_callback(channel, my_callback_two)

# 在通道上添加上升临界值检测，忽略由于开关抖动引起的小于 200ms 的边缘操作
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)
#  或者
GPIO.add_event_callback(channel, my_callback, bouncetime=200)
GPIO.remove_event_detect()

GPIO.remove_event_detect(channel)

import RPi.GPIO as GPIO
# 指定编号规则为BOARD
GPIO.setmode(GPIO.BOARD)
# 将第12个引脚设置为输出模式
GPIO.setup(12, GPIO.OUT)
# 在第12个引脚上创建一个频率为0.5HZ的PWM实例
p = GPIO.PWM(12, 0.5)
# 启用PWM
p.start(1)
input('点击回车停止：')
# 停止PWM
p.stop()
# 释放引脚
GPIO.cleanup()
