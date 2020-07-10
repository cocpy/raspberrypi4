long randNumber;

void setup() {
   Serial.begin(9600);
   // 如果模拟输入引脚0断开，随机模拟
   // 噪声将导致对randomSeed（）的调用生成
   // 每次运行草图时都会有不同的种子编号
   // randomSeed（）将洗牌随机函数
   randomSeed(analogRead(0));
}

void loop() {
   // 从0到299的随机数
   Serial.print("random1=");
   randNumber = random(300);
   Serial.println(randNumber); // 打印0到299之间的随机数
   Serial.print("random2=");
   randNumber = random(10, 20);// 打印一个从10到19的随机数
   Serial.println (randNumber);
   delay(50);
}
