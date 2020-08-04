int buzzer=10;
void setup() {
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(buzzer, OUTPUT); //make the LED pin (13) as output
  
  Serial.println("Hi!, I am Arduino");
 
}
int data;
void loop() {

  data = Serial.read();


if (data == '1')
digitalWrite (buzzer, HIGH);
delay(1000);
digitalWrite (buzzer, LOW);



}
