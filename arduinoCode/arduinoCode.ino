String myCmd;
String myTime;

#include <string.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2); 

//0x27

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

bool findStr(String s,String f){
  String this_str = s;
  String search_str = f;

  // Convert both strings to lowercase to perform a case-insensitive search
  this_str.toLowerCase();
  search_str.toLowerCase();

    if (this_str.indexOf(search_str) != -1) {
      return true;
    } else {
      Serial.println("Did not find");
      return false;
    }

  delay(1000);
}


void loop() {
  // put your main code here, to run repeatedly:
  myCmd=Serial.readStringUntil('\r');
  lcd.clear();  

  if (findStr(myCmd,"%")){
    lcd.setCursor(0,1);
    lcd.print(myCmd+((char)223)+"C");
    lcd.setCursor(0,0);
    lcd.print(" CPU | GPU | TMP");
    delay(100);
  }
  if (findStr(myCmd,":")){
    lcd.setCursor(0,0);
    lcd.print(myCmd.substring(5)+" "+(char)223+"C");
    lcd.setCursor(0,1);
    lcd.print(myCmd.substring(0,5));
  }

  while(Serial.available()==0){

  }
  }
