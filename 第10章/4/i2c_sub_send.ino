#include <Wire.h>
void setup() {
   Wire.begin(2); // 连接地址为2的i2c总线
   Wire.onRequest(requestEvent); // 注册事件
}

Byte x = 0;

void loop() {
   delay(100);
}

// 每当主机请求数据时执行的函数
// 此函数注册为事件，请参阅setup()

void requestEvent() {
   Wire.write(x); // 按照主机的预期，用1字节的消息响应
   x++;
}
