#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 
 long duration,cm;
const int Trig = 9;
const int Echo = 8;
 int n ;

void setup() 

{
  lcd.begin(16, 2);
  Serial.begin(9600);
}


//** Function to Do Nothing**//
void DoNothing()
{
  while(1)
    {
    
    }

}


//*After Object Detected LCD Code*//
void LCD_CameraStart()
  {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Please Wait");
    for(n = 3;n>0 ;n--)
      {
              lcd.setCursor(0,1);
              lcd.clear();
              lcd.print(n);
              delay(1000);
      
      }
  lcd.print("Image Captured");
  DoNothing();
    
  
  }

// ** Before Object Detected LCD Code** //
void LCD()
{
    if(cm<=100)
    {
    lcd.setCursor(0, 0);
  delay(1000);
  lcd.print("HELLO!!,Put Your");
  lcd.setCursor(0,1);
  delay(1000);
  lcd.print("Finger near Cam");
  delay(1000);
  LCD_CameraStart();
    }

    else
    {
      
      }
    
}
  
  

void loop()
{
  
 

  pinMode(Trig, OUTPUT);
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(5);
  digitalWrite(Trig, LOW);

 
  pinMode(Echo, INPUT);
  duration = pulseIn(Echo, HIGH);


cm = microsecondsToCentimeters(duration);
//*** If you want to check the Distance Uncomment the Below Lines ***//
//Serial.print(cm);
//  Serial.print("cm");
//  Serial.println();

delay(100);
  LCD();
    
  }


long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}
