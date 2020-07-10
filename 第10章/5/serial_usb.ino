void setup()
{
  Serial.begin(9600);
}
void loop()
{
  if ( Serial.available())
    {
      if('s' == Serial.read())
        Serial.println("Hello Raspberry,I am Arduino.");
     }
}
