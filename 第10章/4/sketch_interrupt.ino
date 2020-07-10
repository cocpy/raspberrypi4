int pin = 2; //将中断引脚定义为2
volatile int state = LOW; // 确保ISR之间共享变量
//主程序更新正确，声明它们为volatile

void setup() {
   pinMode(13, OUTPUT); //将针脚13设置为输出
   attachInterrupt(digitalPinToInterrupt(pin), blink, CHANGE);
   //当引脚改变值时，中断将调用blink函数
}
void loop() {
   digitalWrite(13, state); //针脚13等于状态值
}

void blink() {
   //ISR 函数
   state = !state; //切换中断发生时的状态
}
