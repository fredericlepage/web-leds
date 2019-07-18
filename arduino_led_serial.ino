int data;
int led_delay = 50;
int n;

void setup(){
  Serial.begin(9600);

  n = 2;
  while (n < 10){
    pinMode(n, OUTPUT);
    digitalWrite(n, LOW);
    n++;
  }
}

void loop(){
  
  while (Serial.available()){
    data = Serial.read();


    if (data == '1'){

      n = 2;
      while (n < 10){
        digitalWrite(n, HIGH);
        delay(led_delay);
        digitalWrite(n, LOW);
        n++;
      }

      while (n > 1) {
        digitalWrite(n, HIGH);
        delay(led_delay);
        n--;
      }
    }

    else if (data == '0'){
      
      n = 9;
      while (n > 1){
        digitalWrite(n, LOW);
        delay(led_delay);
        n--;
      } 
    }
  }
}
