int analogPin = 3; // 传感器连接的引脚
int val = 0; // 变量来存储读取值

void setup() {
   Serial.begin(9600); // 设置序列号
   analogReference(EXTERNAL); // 施加在AREF引脚上的电压（仅0至5V）
      // 用作参考
}

void loop() {
   val = analogRead(analogPin); // 读取输入引脚
   Serial.println(val); // 调试值
}
