String myCmd;
String myTime;
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2); 
//0x27
int a=0;
int stateOfInput = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  lcd.init();
  lcd.clear();         
  lcd.backlight();      // Make sure backlight is on
  
  // Print a message on both lines of the LCD.
  lcd.setCursor(0,0);   //Set cursor to character 2 on line 0
  lcd.print("Booting up...");

}

void loop() {
  // put your main code here, to run repeatedly:


  switch (stateOfInput){
    case 0:
      myCmd=Serial.readStringUntil('\r');
      break;

    default:
      myTime=Serial.readStringUntil('\r');
      break;

  }
 
  while(Serial.available()==0){

  }


  switch (stateOfInput) {
    case 0:
        lcd.clear();
        stateOfInput = 1;
        lcd.setCursor(0,1);
        lcd.print(myCmd+((char)223));
        lcd.setCursor(0,0);
        lcd.print(" CPU | GPU | TMP");
        delay(100);
        break;
    default:
        lcd.setCursor(0,1);
        lcd.print(myCmd+((char)223));
        lcd.setCursor(6,0);
        lcd.print(myTime);
        delay(100);
        stateOfInput = 0;
        break;
  }



}
