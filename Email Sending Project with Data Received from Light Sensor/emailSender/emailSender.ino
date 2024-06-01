char data_rx;

void setup() 
{
  Serial.begin(9600);
}
void loop() 
{
  int buttonPin = analogRead(A0);
  Serial.println(buttonPin);
  delay(3000);
  
  data_rx=Serial.read();
}
