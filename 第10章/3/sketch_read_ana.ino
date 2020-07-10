int analogPin = 3; // 设置引脚
   // 接模拟引脚3
int val = 0; // 变量存储读取的值

void setup() {
   Serial.begin(9600); // 设置序列号
}

void loop() {
   val = analogRead(analogPin); // 读取输入引脚
   Serial.println(val); // 调试值
}
