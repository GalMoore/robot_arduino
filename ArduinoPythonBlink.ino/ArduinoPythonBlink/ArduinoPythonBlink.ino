#define LED 13

// Using http://slides.justen.eng.br/python-e-arduino as refference

void setup() {
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
    digitalWrite(LED, HIGH);
    delay(200);
    digitalWrite(LED, LOW);
    delay(200);
    digitalWrite(LED, HIGH);
    delay(200);
    digitalWrite(LED, LOW);
    delay(200);
    digitalWrite(LED, HIGH);
    delay(200);
    digitalWrite(LED, LOW);
    
}

void loop() {
    if (Serial.available()) {
        char serialListener = Serial.read();
        if (serialListener == 'H') {
            digitalWrite(LED, HIGH);
        }
        else if (serialListener == 'L') {
            digitalWrite(LED, LOW);
        }
    }
}
