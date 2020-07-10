#include <Wire.h> //包含wire库
void setup() {
   Wire.begin(); // 连接i2c总线（主地址可选）
   Serial.begin(9600); // 开始串行输出
}

void loop() {
   Wire.requestFrom(2, 1); // 从设备2请求1字节
   // 从机发送的数据可能少于请求的数量
   while (Wire.available()) {
      char c = Wire.read(); // 接收字节作为字符
      Serial.print(c); // 打印字符
   }
   delay(500);
}
