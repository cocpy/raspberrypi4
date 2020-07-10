void setup() {
   Serial.begin(9600); //将串行库波特率设置为9600
}

void loop() {
   //如果可从中读取字节（字符）
   if(Serial.available()) {
      serial port
      Serial.print("I received:"); //打印内容
      Serial.write(Serial.read()); //发送读取的内容
   }
}
