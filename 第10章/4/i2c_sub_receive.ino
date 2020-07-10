#include <Wire.h> //包含wire库

// 仅运行一次
void setup() {
   Wire.begin(2); // 连接地址为2的i2c总线
   Wire.onReceive(receiveEvent); // 当主机发送任何东西时调用receiveEvent
   Serial.begin(9600); // 开始串行输出以打印接收到的内容
}

void loop() {
   delay(250);
}

//-----每当从主机接收到数据时，此函数都将执行-----//

void receiveEvent(int howMany) {
   // 循环所有，排除最后一个
   while (Wire.available()>1) {
      char c = Wire.read(); // 接收字节作为字符
      Serial.print(c); // 打印字符
   }
}
