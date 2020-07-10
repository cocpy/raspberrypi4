# 引入RPi.GPIO库函数命名为GPIO
import RPi.GPIO as GPIO

# BOARD编号方式，基于插座引脚编号
GPIO.setmode(GPIO.BOARD)

# 定义接口
ENA = 33
IN1 = 35
IN2 = 37

# 设置输出模式
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)

# 将IN1设置为0
GPIO.output(IN1, False)
# 将IN2设置为1
GPIO.output(IN2, True)
# 将ENA设置为1，启动A通道电机
GPIO.output(ENA, True)

# 结束进程，释放GPIO引脚
GPIO.cleanup()