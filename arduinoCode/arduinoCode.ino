String myCmd;
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2); 
//0x27
int a=0;
void setup() {

  Serial.begin(115200);

  lcd.init();
  lcd.clear();         
  lcd.backlight();      
  

  lcd.setCursor(0,0);   
  lcd.print("Booting up...");

}

void loop() {

  myCmd=Serial.readStringUntil('\r');

  while(Serial.available()==0){

  }
  lcd.clear();
  lcd.setCursor(1,1);
  lcd.print(myCmd+((char)223));
  lcd.setCursor(0,0);
  lcd.print(" CPU | GPU | TMP");
  delay(500);


}
