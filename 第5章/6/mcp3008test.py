import RPi.GPIO as GPIO


# ADC上的SPI端口到Cobber，按需修改
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
# DEBUG = 1


# 定义函数
def setup():
    GPIO.setwarnings(False)
    # 指定编号规则为BCM
    GPIO.setmode(GPIO.BCM)
    # 设置SPI接口
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)


def print_message():
    print('|**********************************|')
    print('|   Read MCP3008(3004) ADC value   |')
    print('|   -----------------------------  |')
    print('|    | ADC |           | Pi  |     |')
    print('|    |-----|-----------|-----|     |')
    print('|    | CS  | connect to| CE0 |     |')
    print('|    | Din | connect to| MOSI|     |')
    print('|    | Dout| connect to| MISO|     |')
    print('|    | CLK | connect to| SCLK|     |')
    print('|    | CH0 | connect to| 4.3V|     |')
    print('|    | CH1 | connect to| GND |     |')
    print('|   -----------------------------  |')
    print('|                            OSOYOO|')
    print('|**********************************|\n')
    print('Program is running...')
    print('Please press Ctrl+C to end the program...')
    print('please input 0 to 7...')


# 从MCP3008芯片读取SPI数据，共8个（0到7）可能的adc
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)  # 开始低时钟
    GPIO.output(cspin, False)  # 降低CS

    commandout = adcnum
    commandout |= 0x18  # 起始位+单端位
    commandout <<= 3  # 只需要在这里发送5位
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # 读取一个empty位、一个null位和10个ADC位
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)

    adcout >>= 1  # 第一位为空，所以删除它
    return adcout


# 主函数
def main():
    # print info
    print_message()
    analogChannel = int(input())
    if (analogChannel < 0) or (analogChannel > 7):
        print('input error analogChannel number!')
        print('please input 0 to 7...')
    else:
        adc = readadc(analogChannel, SPICLK, SPIMOSI, SPIMISO, SPICS)
        print('analogChannel %d = %d' % (analogChannel, adc))


# 定义一个清理函数，用于在脚本完成后释放所有内容
def destroy():
    # 释放资源
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        main()
    # 当按下“Ctrl+C”时，将执行子程序destory()方法
    except KeyboardInterrupt:
        destroy()