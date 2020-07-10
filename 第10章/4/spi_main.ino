#include <SPI.h>

void setup (void) {
   Serial.begin(115200); // 将usart的波特率设置为115200
   digitalWrite(SS, HIGH); // 禁用从属选择
   SPI.begin ();
   SPI.setClockDivider(SPI_CLOCK_DIV8);
}

void loop (void) {
   char c;
   digitalWrite(SS, LOW); // 启用从属选择
   // 发送测试字符串
   for (const char * p = "Hello, world!\r" ; c = *p; p++) {
      SPI.transfer (c);
      Serial.print(c);
   }
   digitalWrite(SS, HIGH); // 禁用从属选择
   delay(2000);
}
