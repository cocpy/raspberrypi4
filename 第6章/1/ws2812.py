import time
from neopixel import *
import argparse


# RGB-LED灯条配置
LED_COUNT = 16  # LED数量
LED_PIN = 18  # GPIO18号引脚连接到灯条
# LED_PIN = 10
LED_FREQ_HZ = 800000  # LED信号频率（以赫兹为单位，通常为800khz）
LED_DMA = 10  # 用于生成信号的DMA通道
LED_BRIGHTNESS = 255  # 设置为0（最暗）和255（最亮）
LED_INVERT = False  # 用于反转信号（使用NPN晶体管电平移位时）
LED_CHANNEL = 0  # 对于GPIO 13、19、41、45或53设置为1


# 定义以各种方式为LED动画的功能
def colorWipe(strip, color, wait_ms=50):
    """一次在一个像素上擦除颜色"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """灯光移动动画"""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos):
    """生成彩虹色"""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """雨过天晴"""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """绘制彩虹，均匀分布"""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """消失动画"""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


# 主程序
if __name__ == '__main__':
    # 参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # 创建NeoPixel对象
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # 初始化库
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print('Color wipe animations.')
            colorWipe(strip, Color(255, 0, 0))  # 红
            colorWipe(strip, Color(0, 255, 0))  # 蓝
            colorWipe(strip, Color(0, 0, 255))  # 绿
            print('Theater chase animations.')
            theaterChase(strip, Color(127, 127, 127))  # 白色渐变
            theaterChase(strip, Color(127, 0, 0))  # 红色渐变
            theaterChase(strip, Color(0, 0, 127))  # 蓝色渐变
            print('Rainbow animations.')
            rainbow(strip)
            rainbowCycle(strip)
            theaterChaseRainbow(strip)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
