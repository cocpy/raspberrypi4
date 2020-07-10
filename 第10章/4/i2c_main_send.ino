#include <Wire.h> //包含导线库

//只运行一次
void setup() {
   Wire.begin(); // 连接i2c总线作为主机
}

short age = 0;

void loop() {
   Wire.beginTransmission(2);
   // 传输到设备#2
   Wire.write("age is = ");
   Wire.write(age); // 发送一个字节
   Wire.endTransmission(); // 停止传输
   delay(1000);
}
