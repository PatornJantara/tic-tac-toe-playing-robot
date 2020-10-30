// slave Arduino recieve base and joint 2 angle for control DC Motor 
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bool angle_base_DI_1 = 22;     // to acquire interger from master arduino (0-1023 potentiometer1 value) use 10 for dc motor 1
bool angle_base_DI_2 = 24;
bool angle_base_DI_3 = 26;
bool angle_base_DI_4 = 28;
bool angle_base_DI_5 = 30;
bool angle_base_DI_6 = 32;
bool angle_base_DI_7 = 34;
bool angle_base_DI_8 = 36;
bool angle_base_DI_9 = 38;
bool angle_base_DI_10 = 40;
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bool angle_joint2_DI_1 = 23;  // to acquire interger from master arduino (0-1023 potentiometer2 value) use 10 for dc motor 2
bool angle_joint2_DI_2 = 25;
bool angle_joint2_DI_3 = 27;
bool angle_joint2_DI_4 = 29;
bool angle_joint2_DI_5 = 31;
bool angle_joint2_DI_6 = 33;
bool angle_joint2_DI_7 = 35;
bool angle_joint2_DI_8 = 37;
bool angle_joint2_DI_9 = 39;
bool angle_joint2_DI_10 = 41;

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bool pwmPin_base_left = 9;   // set PWM pin of BTS7960 dc motor driver
bool pwmPin_base_right = 8;
bool pwmPin_joint2_up = 10;
bool pwmPin_joint2_down = 11;

int currentAngle_base;      //  value from reading potentiometer in base
int currentAngle_joint2;    //  value from reading potentiometer in joint 2

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

int requiredAngle_base;     // to convert digital input to angle value of base use 10 pin
bool requiredAngle_base_1;
bool requiredAngle_base_2;
bool requiredAngle_base_3;
bool requiredAngle_base_4;
bool requiredAngle_base_5;
bool requiredAngle_base_6;
bool requiredAngle_base_7;
bool requiredAngle_base_8;
bool requiredAngle_base_9;
bool requiredAngle_base_10;
//---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
int requiredAngle_joint2;   // to convert digital input to angle value of joint 2 use 10 pin
bool requiredAngle_joint2_1;
bool requiredAngle_joint2_2;
bool requiredAngle_joint2_3;
bool requiredAngle_joint2_4;
bool requiredAngle_joint2_5;
bool requiredAngle_joint2_6;
bool requiredAngle_joint2_7;
bool requiredAngle_joint2_8;
bool requiredAngle_joint2_9;
bool requiredAngle_joint2_10;
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
int errorAmount_base;     // different of current angle and required angle of base
int errorAmount_joint2;   // different of current angle and required angle of joint 2
int remappedErrorAmount_base;  //  scale error to PWM motor 1 (base) 
int remappedErrorAmount_joint2;//  scale error to PWM motor 2  (joint 2)

byte acceptableError = 2; // for smoothly because analogread from potentiometer not stable
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void setup()
{
  Serial.begin(9600); // set buard rate 

 // set input / output
  pinMode(angle_base_DI_1,INPUT);
  pinMode(angle_base_DI_2,INPUT);
  pinMode(angle_base_DI_3,INPUT);
  pinMode(angle_base_DI_4,INPUT);
  pinMode(angle_base_DI_5,INPUT);
  pinMode(angle_base_DI_6,INPUT);
  pinMode(angle_base_DI_7,INPUT);
  pinMode(angle_base_DI_8,INPUT);
  pinMode(angle_base_DI_9,INPUT);
  pinMode(angle_base_DI_10,INPUT);
  
  pinMode(angle_joint2_DI_1,INPUT);
  pinMode(angle_joint2_DI_2,INPUT);
  pinMode(angle_joint2_DI_3,INPUT);
  pinMode(angle_joint2_DI_4,INPUT);
  pinMode(angle_joint2_DI_5,INPUT);
  pinMode(angle_joint2_DI_6,INPUT);
  pinMode(angle_joint2_DI_7,INPUT);
  pinMode(angle_joint2_DI_8,INPUT);
  pinMode(angle_joint2_DI_9,INPUT);
  pinMode(angle_joint2_DI_10,INPUT);
  
  pinMode(pwmPin_base_left, OUTPUT);
  pinMode(pwmPin_base_right, OUTPUT);
  pinMode(pwmPin_joint2_up, OUTPUT);
  pinMode(pwmPin_joint2_down, OUTPUT);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  

}
// acquire base angle from DI/DO master arduino
void acquire_baseAngle(){
  requiredAngle_base_1=digitalRead(angle_base_DI_1);
  requiredAngle_base_2=digitalRead(angle_base_DI_2);
  requiredAngle_base_3=digitalRead(angle_base_DI_3);
  requiredAngle_base_4=digitalRead(angle_base_DI_4);
  requiredAngle_base_5=digitalRead(angle_base_DI_5);
  requiredAngle_base_6=digitalRead(angle_base_DI_6);
  requiredAngle_base_7=digitalRead(angle_base_DI_7);
  requiredAngle_base_8=digitalRead(angle_base_DI_8);
  requiredAngle_base_9=digitalRead(angle_base_DI_9);
  requiredAngle_base_10=digitalRead(angle_base_DI_10);
  requiredAngle_base = (requiredAngle_base_1)+(requiredAngle_base_2*2)+(requiredAngle_base_3*4)+(requiredAngle_base_4*8)+(requiredAngle_base_5*16)
                        +(requiredAngle_base_6*32)+(requiredAngle_base_7*64)+(requiredAngle_base_8*128)+(requiredAngle_base_9*256)+(requiredAngle_base_10*512);
}
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// acquire joint 2 angle from DI/DO master arduino
void acquire_joint2Angle(){
  requiredAngle_joint2_1=digitalRead(angle_joint2_DI_1);
  requiredAngle_joint2_2=digitalRead(angle_joint2_DI_2);
  requiredAngle_joint2_3=digitalRead(angle_joint2_DI_3);
  requiredAngle_joint2_4=digitalRead(angle_joint2_DI_4);
  requiredAngle_joint2_5=digitalRead(angle_joint2_DI_5);
  requiredAngle_joint2_6=digitalRead(angle_joint2_DI_6);
  requiredAngle_joint2_7=digitalRead(angle_joint2_DI_7);
  requiredAngle_joint2_8=digitalRead(angle_joint2_DI_8);
  requiredAngle_joint2_9=digitalRead(angle_joint2_DI_9);
  requiredAngle_joint2_10=digitalRead(angle_joint2_DI_10);
  requiredAngle_joint2 = (requiredAngle_joint2_1)+(requiredAngle_joint2_2*2)+(requiredAngle_joint2_3*4)+(requiredAngle_joint2_4*8)+(requiredAngle_joint2_5*16)
                        +(requiredAngle_joint2_6*32)+(requiredAngle_joint2_7*64)+(requiredAngle_joint2_8*128)+(requiredAngle_joint2_9*256)+(requiredAngle_joint2_10*512);                      
  
}
  //----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void loop()
{ 
  acquire_baseAngle();    // read base angle integer from master arduino 
  acquire_joint2Angle();  // read joint 2 angle integer from master arduino 
  
  if(requiredAngle_base <= 300)  // to define range
  {
    requiredAngle_base = 300;
    }
   if(requiredAngle_base >= 800)  // to limit range 
  {
    requiredAngle_base = 800;
    }    
  if(requiredAngle_joint2 <= 500)
  {
    requiredAngle_joint2 = 500;
    }
  if(requiredAngle_joint2 >= 900)
  {
    requiredAngle_joint2 = 900;
    }      
 //----------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
  //Serial.println( currentAngle_base);
  //Serial.println( currentAngle_joint2);
  //Serial.println(requiredAngle_base);
  //Serial.println(requiredAngle_joint2);
  
 //---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
  currentAngle_base = analogRead(0);   // read and condition current base angle
  if (currentAngle_base >= 800){
   currentAngle_base =800;
   requiredAngle_base=800; 
  } if (currentAngle_base <= 300) {
   currentAngle_base =300;
   requiredAngle_base =300; 
  }

  currentAngle_joint2 = analogRead(1);  // read and condition current joint 2 angle
  if (currentAngle_joint2 >= 900){
   currentAngle_joint2 =900;
   requiredAngle_joint2=900; 
  } if (currentAngle_joint2 <= 500) {
   currentAngle_joint2 =500;
   requiredAngle_joint2 =500; 
  }
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
  errorAmount_base=abs(currentAngle_base - requiredAngle_base );   // to control PWM value of base motor driver
  remappedErrorAmount_base=map(errorAmount_base ,0, 320 , 7, 220 ); //(pin,0, max range, minPWM, maxPWM)
  if (remappedErrorAmount_base < acceptableError){
      remappedErrorAmount_base =0;
}
  errorAmount_joint2=abs(currentAngle_joint2 - requiredAngle_joint2 ); // to control PWM value of joint 2 motor driver
  remappedErrorAmount_joint2=map(errorAmount_joint2 ,0, 200 , 7, 170 );
  if (remappedErrorAmount_joint2 < acceptableError){
      remappedErrorAmount_joint2 =0;
  }
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// set direction of base motor 
  if (currentAngle_base < requiredAngle_base){        
  analogWrite(pwmPin_base_right,0); //8
  analogWrite(pwmPin_base_left,remappedErrorAmount_base); //9
  
  } if (currentAngle_base > requiredAngle_base){ 
  analogWrite(pwmPin_base_left,0); 
  analogWrite(pwmPin_base_right,remappedErrorAmount_base);  
  }
// set direction of joint 2 motor     
  if (currentAngle_joint2 < requiredAngle_joint2){
  analogWrite(pwmPin_joint2_down,0);  //11
  analogWrite(pwmPin_joint2_up,remappedErrorAmount_joint2); //10
  
  } if (currentAngle_joint2>requiredAngle_joint2){
  analogWrite(pwmPin_joint2_up,0);
  analogWrite(pwmPin_joint2_down,remappedErrorAmount_joint2);
  
  }
 }


