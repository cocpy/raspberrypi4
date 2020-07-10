#include <Wire.h>

int a;

void setup() {
  Wire.begin(8);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
  pinMode(11,OUTPUT);
}

void loop() {
  delay(100);
}


void receiveEvent(int howMany)
{
  while (Wire.available())
  {
    a = Wire.read();
    analogWrite(11,a);
    Serial.println(a);
  }
}
