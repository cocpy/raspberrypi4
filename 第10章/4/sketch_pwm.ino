int ledPin = 9; // LED连接到数字引脚9
int analogPin = 3; // 电位计连接到模拟针脚3
int val = 0; // 变量来存储读取值

void setup() {
   pinMode(ledPin, OUTPUT); // 将管脚设置为输出
}

void loop() {
   val = analogRead(analogPin); // 读取输入引脚
   analogWrite(ledPin, (val / 4)); // analogRead值从0到1023
      // 模拟写入0到255的值
}
