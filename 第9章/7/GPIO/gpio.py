from ctypes import *
import time

# 调用C语言编写的模块，先确定该文件在同级目录下
gpio = CDLL('./SC16IS752GPIO.so')
OUT = 1
IN  = 0

# 初始化0-7号GPIO接口
gpio.SC16IS752GPIO_Init()

# 调用SC16IS752GPIO_Mode(int Pin, int Mode)方法
# 引脚范围: 0-7
# 模式:0 = 输入, 1 = 输出
gpio.SC16IS752GPIO_Mode(0, OUT)
gpio.SC16IS752GPIO_Mode(1, IN)

# 写入值
# 调用SC16IS752GPIO_Write(int Pin, int value)方法
# 引脚范围: 0-7
# 值:0 = 低电平信号, 1 = 高电平信号
i = 0
for i in range(0, 10):
    gpio.SC16IS752GPIO_Write(0, i % 2)
    time.sleep(1)
    
# 读取值
# 调用SC16IS752GPIO_Read(int Pin)方法
# 引脚范围: 0-7
gpio.SC16IS752GPIO_Read(1)
print("GPIO 1 = "),gpio.SC16IS752GPIO_Read(1)

# 退出
# gpio.SC16IS752GPIO_Exit()
