int trigPin1=2;
int echoPin1=3;
int trigPin2=4;
int echoPin2=5;
int trigPin3=7;
int echoPin3=6;
int aux=0;
void setup() {
  Serial.begin (9600);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);

}

void loop() {
  long d;
  noTone(11);
  d=sensor(trigPin3,echoPin3);
  if(d<100){
    tone(11,300,30);}
  delay(1);
  
  d=sensor(trigPin2,echoPin2);
  if(d<50){
    tone(11,300, 30);}
  delay(1);
  
  d=sensor(trigPin1,echoPin1);
  if(aux-d>15){
    Serial.println("STEP"); // se envia al rasberry pi
  }
  delay(1);
  aux=d;
}

long sensor(int trigPin, int echoPin){
  long d;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  d = pulseIn(echoPin, HIGH);
  d = d/58.2;
  return d;
}
