import time

import RPi.GPIO as GPIO


# 连接DO使用的引脚
DO_PIN = 17
# 连接AO使用的ADC通道0
AO_PIN = 0
# 连接ADC使用的引脚
SPI_CS = 8
SPI_MISO = 9
SPI_MOSI = 10
SPI_CLK = 11


def init():
    """初始化方法"""
    # 忽略警告
    GPIO.setwarnings(False)
    # 设置编号方式
    GPIO.setmode(GPIO.BCM)
    # GPIO.output(buzzer,GPIO.HIGH)
    # 设置为输入模式
    GPIO.setup(DO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # 设置ADC使用的引脚
    GPIO.setup(SPI_MISO, GPIO.IN)
    GPIO.setup(SPI_MOSI, GPIO.OUT)
    GPIO.setup(SPI_CLK, GPIO.OUT)
    GPIO.setup(SPI_CS, GPIO.OUT)


def get_adc(adc_num, clock_pin, mosi_pin, miso_pin, cs_pin):
    """从ADC读取参数"""
    if (adc_num > 7) or (adc_num < 0):
        # 校验数据
        return -1

    # 拉低各接口的电平
    GPIO.output(cs_pin, True)
    GPIO.output(clock_pin, False)
    GPIO.output(cs_pin, False)

    command_out = adc_num
    # 起始位+输出位
    command_out |= 0x18
    # 只需发送5位
    command_out <<= 3
    for i in range(5):
        if command_out & 0x80:
            GPIO.output(mosi_pin, True)
        else:
            GPIO.output(mosi_pin, False)
        command_out <<= 1
        GPIO.output(clock_pin, True)
        GPIO.output(clock_pin, False)

    # ADC输出
    adc_out = 0

    # 读入一个空位，一个null位和10个ADC位
    for i in range(12):
        GPIO.output(clock_pin, True)
        GPIO.output(clock_pin, False)
        adc_out <<= 1
        if GPIO.input(miso_pin):
            adc_out |= 0x1

    GPIO.output(cs_pin, True)
    # 第一位为“null”，因此将其删除
    adc_out >>= 1
    return adc_out


def main_loop():
    """主循环，打印读取到的数据"""
    # 初始化
    init()
    # 预热
    time.sleep(3)
    while True:
        # 从ADC读取参数
        flame_value = get_adc(AO_PIN, SPI_CLK, SPI_MOSI, SPI_MISO, SPI_CS)
        if GPIO.input(DO_PIN):
            print("检测到火焰，ADC值为：", str("%.1f" % ((1024 - flame_value) / 1024. * 3.3)) + "V")
            time.sleep(1)
        else:
            print("未检测到火焰")
            time.sleep(1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("程序结束！")
    finally:
        GPIO.cleanup()
