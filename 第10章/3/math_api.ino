double double__x = 45.45 ;
double double__y = 30.20 ;

void setup() {
   Serial.begin(9600);
   Serial.print("cos num = ");
   Serial.println (cos (double__x) ); // 返回x的余弦
   Serial.print("absolute value of num = ");
   Serial.println (fabs (double__x) ); // 浮点数的绝对值
   Serial.print("floating point modulo = ");
   Serial.println (fmod (double__x, double__y)); // 浮点模
   Serial.print("sine of num = ");
   Serial.println (sin (double__x) ) ;// 返回x的正弦值
   Serial.print("square root of num : ");
   Serial.println ( sqrt (double__x) );// 返回x的平方根
   Serial.print("tangent of num : ");
   Serial.println ( tan (double__x) ); // 返回x的正切值
   Serial.print("exponential value of num : ");
   Serial.println ( exp (double__x) ); // 函数返回x的指数值
   Serial.print("cos num : ");

   Serial.println (atan (double__x) ); // x的反正切
   Serial.print("tangent of num : ");
   Serial.println (atan2 (double__y, double__x) );// y/x的反正切
   Serial.print("arc tangent of num : ");
   Serial.println (log (double__x) ) ; // 自然对数x
   Serial.print("cos num : ");
   Serial.println ( log10 (double__x)); // x的对数，以10为底
   Serial.print("logarithm of num to base 10 : ");
   Serial.println (pow (double__x, double__y) );// x对y的幂
   Serial.print("power of num : ");
   Serial.println (square (double__x)); // x的平方
}

void loop() {

}
