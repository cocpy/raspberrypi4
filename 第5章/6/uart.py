import serial


pl = serial.Serial("/dev/ttyAMA0", baudrate=9600)
pl.open()
pl.write(bytes("UART", "utf-8"))
