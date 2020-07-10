#include <SPI.h>
char buff [50];
volatile byte indx;
volatile boolean process;

void setup (void) {
   Serial.begin (115200);
   pinMode(MISO, OUTPUT); // 必须在主机上发送，以便将其设置为输出
   SPCR |= _BV(SPE); // 在从属模式下打开SPI
   indx = 0; // 缓冲区清空
   process = false;
   SPI.attachInterrupt(); // 打开中断
}
// SPI中断程序
ISR (SPI_STC_vect) {
   byte c = SPDR; // 从SPI数据寄存器读取字节
   if (indx < sizeof buff) {
      buff [indx++] = c; // 在数组buff的下一个索引中保存数据
      if (c == '\r') // 检查单词的结尾
      process = true;
   }
}

void loop (void) {
   if (process) {
      process = false; // 重置进程
      Serial.println (buff); // 在串行监视器上打印阵列
      indx= 0; // 重置按钮为零
   }
}
