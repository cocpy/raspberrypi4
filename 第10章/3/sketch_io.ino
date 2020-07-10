int button = 5 ; // 连接到针脚5的按钮
int LED = 6; // LED连接至针脚6

void setup () {
   pinMode(button , INPUT_PULLUP);
   // 设置数字引脚作为上拉电阻的输入
   pinMode(button , OUTPUT); // 将数字管脚设置为输出
}

void setup () {
   // 如果按下按钮
   If (digitalRead(button ) == LOW) {
      digitalWrite(LED,HIGH); // 点亮led
      delay(500); // 延时500ms
      digitalWrite(LED,LOW); // 熄灭led
      delay(500); // 延时500ms
   }
}
