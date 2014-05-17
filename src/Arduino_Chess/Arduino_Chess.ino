int ttl1 = 3;
int ttl2 = 4;
int ttl3 = 5;
int ttl4 = 6;
int ttl5 = 7;
int ttl6 = 8;
int ttl7 = 9;
int ttl8 = 10;
byte ttlout = B10000000;
boolean tmp;
int i=0;
int ttloutstr;

void setup() {
  //pinMode(led, OUTPUT);  
  pinMode(ttl1, OUTPUT);   
  pinMode(ttl2, OUTPUT);   
  pinMode(ttl3, OUTPUT);  
  pinMode(ttl4, OUTPUT);
  pinMode(ttl5, OUTPUT);
  pinMode(ttl6, OUTPUT);
  pinMode(ttl7, OUTPUT);
  pinMode(ttl8, INPUT);
  Serial.begin(9600);
}

void loop() {
  while(ttl8 == HIGH){
    delay(1); 
  }
    
  String readString;
  
  while (Serial.available()) {
    delay(3); 
    if (Serial.available() >0) {
      char c = Serial.read();  
      readString += c;
    } 
  }
  
  if ( readString.length() > 0) {
    ttlout = reconstruct_byte( readString);

    tmp = B01000000 & ttlout;
    digitalWrite(ttl1, tmp);
    tmp = B00100000 & ttlout;
    digitalWrite(ttl2, tmp);
    tmp = B00010000 & ttlout;
    digitalWrite(ttl3, tmp);
    tmp = B00001000 & ttlout;
    digitalWrite(ttl4, tmp);
    tmp = B00000100 & ttlout;
    digitalWrite(ttl5, tmp);
    tmp = B00000010 & ttlout;
    digitalWrite(ttl6, tmp);
    tmp = B00000001 & ttlout;
    digitalWrite(ttl7, tmp);
    delay(5000);
  }else{
    digitalWrite(ttl1, HIGH);
    digitalWrite(ttl2, HIGH);
    digitalWrite(ttl3, HIGH);
    digitalWrite(ttl4, HIGH);
    digitalWrite(ttl5, HIGH);
    digitalWrite(ttl6, HIGH);
    digitalWrite(ttl7, LOW);
  }

byte reconstruct_byte(String serial_input){
  byte signal=0;

  for (int j=0; j<serial_input.length(); j++){
    signal = signal* B10;
    if (serial_input[j] == '1'){
       signal = signal+B1;
    }
  }

  return signal;
}
