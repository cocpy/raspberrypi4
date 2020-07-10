import ADS1256
import RPi.GPIO as GPIO


try:
    ADC = ADS1256.ADS1256()  # 创建ADS实例
    ADC.ADS1256_init()  # 初始化

    while (1):
        ADC_Value = ADC.ADS1256_GetAll()  # 读取所有通道数值
        print("0 ADC = %lf" % (ADC_Value[0] * 5.0 / 0x7fffff))
        print("1 ADC = %lf" % (ADC_Value[1] * 5.0 / 0x7fffff))
        print("2 ADC = %lf" % (ADC_Value[2] * 5.0 / 0x7fffff))
        print("3 ADC = %lf" % (ADC_Value[3] * 5.0 / 0x7fffff))
        print("4 ADC = %lf" % (ADC_Value[4] * 5.0 / 0x7fffff))
        print("5 ADC = %lf" % (ADC_Value[5] * 5.0 / 0x7fffff))
        print("6 ADC = %lf" % (ADC_Value[6] * 5.0 / 0x7fffff))
        print("7 ADC = %lf" % (ADC_Value[7] * 5.0 / 0x7fffff))
        print("\33[9A")
except:
    GPIO.cleanup()
    print("\r\nProgram end     ")
    exit()
