int incomingByte = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    if (incomingByte == 97) {
      Serial.println("lights_on");
      digitalWrite(13, HIGH);
    }else{
      Serial.println("lights_off");
      digitalWrite(13, LOW);
    }
  }
  //delay(1000);
  //Serial.println("a");
}
