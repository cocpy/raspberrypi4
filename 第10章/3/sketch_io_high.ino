int LED = 6; // LED连接到针脚6

void setup () {
   pinMode(LED, OUTPUT); // 将数字管脚设置为输出
}

void setup () {
   digitalWrite(LED,HIGH); // 点亮led
   delay(500); // 延时500ms
   digitalWrite(LED,LOW); // 熄灭led
   delay(500); // 延时500ms
}
