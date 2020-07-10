import RPi.GPIO as GPIO
# sudo pip3 install pyserial
import serial
import time

ser = serial.Serial("/dev/ttyS0",115200)
ser.flushInput()

phone_number = '10010'  # 电话号码，按需更改
text_message = 'www.raspberrypi.org'  # 短信内容
power_key = 6
rec_buff = ''

# 发送AT命令
def send_at(command,back,timeout):
	rec_buff = ''
	ser.write((command+'\r\n').encode())
	time.sleep(timeout)
	if ser.inWaiting():
		time.sleep(0.01 )
		rec_buff = ser.read(ser.inWaiting())
	if back not in rec_buff.decode():
		print(command + ' ERROR')
		print(command + ' back:\t' + rec_buff.decode())
		return 0
	else:
		print(rec_buff.decode())
		return 1

# 发送短信
def SendShortMessage(phone_number,text_message):
	
	print("Setting SMS mode...")
	send_at("AT+CMGF=1","OK",1)
	print("Sending Short Message")
	answer = send_at("AT+CMGS=\""+phone_number+"\"",">",2)
	if 1 == answer:
		ser.write(text_message.encode())
		ser.write(b'\x1A')
		answer = send_at('','OK',20)
		if 1 == answer:
			print('send successfully')
		else:
			print('error')
	else:
		print('error%d'%answer)

# 接收短信
def ReceiveShortMessage():
	rec_buff = ''
	print('Setting SMS mode...')
	send_at('AT+CMGF=1','OK',1)
	send_at('AT+CPMS=\"SM\",\"SM\",\"SM\"', 'OK', 1)
	answer = send_at('AT+CMGR=1','+CMGR:',2)
	if 1 == answer:
		answer = 0
		if 'OK' in rec_buff:
			answer = 1
			print(rec_buff)
	else:
		print('error%d'%answer)
		return False
	return True

# 开启
def power_on(power_key):
	print('SIM7600X is starting:')
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(power_key,GPIO.OUT)
	time.sleep(0.1)
	GPIO.output(power_key,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(power_key,GPIO.LOW)
	time.sleep(20)
	ser.flushInput()
	print('SIM7600X is ready')

# 关机
def power_down(power_key):
	print('SIM7600X is loging off:')
	GPIO.output(power_key,GPIO.HIGH)
	time.sleep(3)
	GPIO.output(power_key,GPIO.LOW)
	time.sleep(18)
	print('Good bye')

try:
	power_on(power_key)
	print('Sending Short Message Test:')
	SendShortMessage(phone_number,text_message)
	print('Receive Short Message Test:\n')
	print('Please send message to phone ' + phone_number)
	ReceiveShortMessage()
	power_down(power_key)
except :
	if ser != None:
		ser.close()
	GPIO.cleanup()
