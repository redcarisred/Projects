#include <Wire.h>
#include "Adafruit_TCS34725.h"
bool buttonState=LOW;
#define redpin 9
#define greenpin 10
#define bluepin 11
#define buttonpin 4
#define commonAnode false
byte gammatable[256];


Adafruit_TCS34725 tcs = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);

void setup() {
  Serial.begin(9600);
  if (tcs.begin()) {
    Serial.println("Sensor found.");
  } else {
    Serial.println("Sensor not found...");
    while (1); // halt!
  }
  
  pinMode(redpin, OUTPUT);
  pinMode(greenpin, OUTPUT);
  pinMode(bluepin, OUTPUT);
  pinMode(buttonpin, INPUT);
  for (int i=0; i<256; i++) {
    float x = i;
    x /= 255;
    x = pow(x, 2.5);
    x *= 255;
      
    if (commonAnode) {
      gammatable[i] = 255 - x;
    } else {
      gammatable[i] = x;      
    }
    //Serial.println(gammatable[i]);
  }
}

void loop() {
  buttonState = digitalRead(buttonpin);
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    uint16_t clear, red, green, blue;
  
    tcs.setInterrupt(false);      // turn on LED
  
    delay(60);  // takes 50ms to read 
    
    tcs.getRawData(&red, &green, &blue, &clear);
  
    tcs.setInterrupt(true); 
    
    Serial.print(red);
    Serial.print(' ');
    Serial.print(green);
    Serial.print(' ');
    Serial.print(blue);
    Serial.println();
    uint32_t sum = clear;
    float r, g, b;
    r = red; r /= sum;
    g = green; g /= sum;
    b = blue; b /= sum;
    r *= 256; g *= 256; b *= 256;
    
    analogWrite(redpin, gammatable[(int)r]);
    analogWrite(greenpin, gammatable[(int)g]);
    analogWrite(bluepin, gammatable[(int)b]);
    delay(5000);
  }
}
