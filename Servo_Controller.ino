 // master Arduino / python reciever  
 //---------------------------------------------------------------------------------------------------------------------------------
#include <Servo.h>  // call servo library
char python ;       // use char for read as character
int turn = 0;    
int base_offset = -20;  //  to adjust offset angles to old home position --- Can be variable value by using potentiometer or knob
int joint2_offset = -28;   
//---------------------------------------------------------------------------------------------------------------------------------
// define servo command name

Servo joint_3;
Servo joint_4;
Servo wrist ;
Servo gripper;
//---------------------------------------------------------------------------------------------------------------------------------

// integer to bit of base angle      
int base_angle_DO = 470 ;
byte angle_base_DO_1_write;
byte angle_base_DO_2_write;
byte angle_base_DO_3_write;
byte angle_base_DO_4_write;
byte angle_base_DO_5_write;
byte angle_base_DO_6_write;
byte angle_base_DO_7_write;
byte angle_base_DO_8_write;
byte angle_base_DO_9_write;
byte angle_base_DO_10_write;
//---------------------------------------------------------------------------------------------------------------------------------

// Pin which use to send base angle value
byte angle_base_DO_1 = 22;
byte angle_base_DO_2 = 24;
byte angle_base_DO_3 = 26;
byte angle_base_DO_4 = 28;
byte angle_base_DO_5 = 30;
byte angle_base_DO_6 = 32;
byte angle_base_DO_7 = 34;
byte angle_base_DO_8 = 36;
byte angle_base_DO_9 = 38;
byte angle_base_DO_10 = 40;
//---------------------------------------------------------------------------------------------------------------------------------

//integer to bit of joint 2 angle

int angle_joint2_DO = 780 ;
byte angle_joint2_DO_1_write;
byte angle_joint2_DO_2_write;
byte angle_joint2_DO_3_write;
byte angle_joint2_DO_4_write;
byte angle_joint2_DO_5_write;
byte angle_joint2_DO_6_write;
byte angle_joint2_DO_7_write;
byte angle_joint2_DO_8_write;
byte angle_joint2_DO_9_write;
byte angle_joint2_DO_10_write;

//---------------------------------------------------------------------------------------------------------------------------------

// Pin which use to send joint 2 angle value

byte angle_joint2_DO_1 = 23;
byte angle_joint2_DO_2 = 25;
byte angle_joint2_DO_3 = 27;
byte angle_joint2_DO_4 = 29;
byte angle_joint2_DO_5 = 31;
byte angle_joint2_DO_6 = 33;
byte angle_joint2_DO_7 = 35;
byte angle_joint2_DO_8 = 37;
byte angle_joint2_DO_9 = 39;
byte angle_joint2_DO_10 = 41;

 //---------------------------------------------------------------------------------------------------------------------------------
void setup()
{  
  Serial.begin(9600);  // set buard rate
// set servo pin 
  joint_3.attach(8);
  joint_4.attach(9);
  wrist.attach(11);
  gripper.attach(13);
// set input / output  
  pinMode(angle_base_DO_1,OUTPUT);
  pinMode(angle_base_DO_2,OUTPUT);
  pinMode(angle_base_DO_3,OUTPUT);
  pinMode(angle_base_DO_4,OUTPUT);
  pinMode(angle_base_DO_5,OUTPUT);
  pinMode(angle_base_DO_6,OUTPUT);
  pinMode(angle_base_DO_7,OUTPUT);
  pinMode(angle_base_DO_8,OUTPUT);
  pinMode(angle_base_DO_9,OUTPUT);
  pinMode(angle_base_DO_10,OUTPUT);

  pinMode(angle_joint2_DO_1,OUTPUT);
  pinMode(angle_joint2_DO_2,OUTPUT);
  pinMode(angle_joint2_DO_3,OUTPUT);
  pinMode(angle_joint2_DO_4,OUTPUT);
  pinMode(angle_joint2_DO_5,OUTPUT);
  pinMode(angle_joint2_DO_6,OUTPUT);
  pinMode(angle_joint2_DO_7,OUTPUT);
  pinMode(angle_joint2_DO_8,OUTPUT);
  pinMode(angle_joint2_DO_9,OUTPUT);
  pinMode(angle_joint2_DO_10,OUTPUT);

//---------------------------------------------------------------------------------------------------------------------------------
// Initail position 

  joint_3.write(20);
  joint_4.write(20);
  wrist.write(0);
  gripper.write(180);
  base_angle_DO =475+base_offset;
  angle_joint2_DO = 780+joint2_offset;
  base_angle_DO_calculation ();     
  joint2_angle_DO_calculation();    
  base_angle_DO_write ();        
  joint_2_angle_DO_write (); 
  
}
  //---------------------------------------------------------------------------------------------------------------------------------
void base_angle_DO_calculation (){
  
  angle_base_DO_1_write = base_angle_DO%2;
  base_angle_DO=base_angle_DO/2;
  angle_base_DO_2_write = base_angle_DO%2;
  base_angle_DO=base_angle_DO/2;
  angle_base_DO_3_write = base_angle_DO%2;
  base_angle_DO=base_angle_DO/2;
  angle_base_DO_4_write = base_angle_DO%2;
  base_angle_DO=base_angle_DO/2;
  angle_base_DO_5_write = base_angle_DO%2;
  base_angle_DO=base_angle_DO/2;
  angle_base_DO_6_write = base_angle_DO%2;
  base_angle_DO=base_angle_DO/2;
  angle_base_DO_7_write = base_angle_DO%2;
  base_angle_DO=base_angle_DO/2;
  angle_base_DO_8_write = base_angle_DO%2;
  base_angle_DO=base_angle_DO/2;
  angle_base_DO_9_write = base_angle_DO%2;
  base_angle_DO=base_angle_DO/2;
  angle_base_DO_10_write = base_angle_DO%2;

}
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void joint2_angle_DO_calculation(){
  
  angle_joint2_DO_1_write = angle_joint2_DO%2;
  angle_joint2_DO = angle_joint2_DO/2;
  angle_joint2_DO_2_write = angle_joint2_DO%2;
  angle_joint2_DO = angle_joint2_DO/2;
  angle_joint2_DO_3_write = angle_joint2_DO%2;
  angle_joint2_DO = angle_joint2_DO/2;
  angle_joint2_DO_4_write = angle_joint2_DO%2;
  angle_joint2_DO = angle_joint2_DO/2;
  angle_joint2_DO_5_write = angle_joint2_DO%2;
  angle_joint2_DO = angle_joint2_DO/2;
  angle_joint2_DO_6_write = angle_joint2_DO%2;
  angle_joint2_DO = angle_joint2_DO/2;
  angle_joint2_DO_7_write = angle_joint2_DO%2;
  angle_joint2_DO = angle_joint2_DO/2;
  angle_joint2_DO_8_write = angle_joint2_DO%2;
  angle_joint2_DO = angle_joint2_DO/2;
  angle_joint2_DO_9_write = angle_joint2_DO%2;
  angle_joint2_DO = angle_joint2_DO/2;
  angle_joint2_DO_10_write = angle_joint2_DO%2;

}
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void base_angle_DO_write (){
  digitalWrite(angle_base_DO_1,angle_base_DO_1_write);
  digitalWrite(angle_base_DO_2,angle_base_DO_2_write);
  digitalWrite(angle_base_DO_3,angle_base_DO_3_write);
  digitalWrite(angle_base_DO_4,angle_base_DO_4_write);
  digitalWrite(angle_base_DO_5,angle_base_DO_5_write);
  digitalWrite(angle_base_DO_6,angle_base_DO_6_write);
  digitalWrite(angle_base_DO_7,angle_base_DO_7_write);
  digitalWrite(angle_base_DO_8,angle_base_DO_8_write);
  digitalWrite(angle_base_DO_9,angle_base_DO_9_write);
  digitalWrite(angle_base_DO_10,angle_base_DO_10_write);        
}
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void joint_2_angle_DO_write (){
  digitalWrite(angle_joint2_DO_1,angle_joint2_DO_1_write);
  digitalWrite(angle_joint2_DO_2,angle_joint2_DO_2_write);
  digitalWrite(angle_joint2_DO_3,angle_joint2_DO_3_write);
  digitalWrite(angle_joint2_DO_4,angle_joint2_DO_4_write);
  digitalWrite(angle_joint2_DO_5,angle_joint2_DO_5_write);
  digitalWrite(angle_joint2_DO_6,angle_joint2_DO_6_write);
  digitalWrite(angle_joint2_DO_7,angle_joint2_DO_7_write);
  digitalWrite(angle_joint2_DO_8,angle_joint2_DO_8_write);
  digitalWrite(angle_joint2_DO_9,angle_joint2_DO_9_write);
  digitalWrite(angle_joint2_DO_10,angle_joint2_DO_10_write);        
}
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void home_position () {
  angle_joint2_DO = 650+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write ();
  delay(2000);
  joint_3.write(50);
  delay(1000);
  angle_joint2_DO = 780+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write ();
  delay(2000);
  joint_3.write(20);
  delay(1000);
  joint_4.write(20);
  delay(1000); 
  base_angle_DO =475+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();  
  
  }
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void pick (){

  if(turn > 4)
  {
  turn = 4;  
  }
  if(turn == 1){
  base_angle_DO =354+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2000);
  joint_4.write(65);
  delay(1000);
  angle_joint2_DO = 660+joint2_offset;   
  joint2_angle_DO_calculation();  
  joint_2_angle_DO_write ();    
   delay(2000);
  }
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
  if(turn == 2){
  base_angle_DO =572+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2000);
  joint_4.write(76);
  delay(1000);
  angle_joint2_DO = 640+joint2_offset;   
  joint2_angle_DO_calculation();  
  joint_2_angle_DO_write ();    
   delay(2000);
  }
  //----------------------------------------------------------------------------------------------------------------------------------------------
  if(turn == 3){
  base_angle_DO =553+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2000);
  joint_3.write(30);
  delay(1000);
  joint_4.write(100);
  delay(1000);
  angle_joint2_DO = 612+joint2_offset;   
  joint2_angle_DO_calculation();  
  joint_2_angle_DO_write ();    
  delay(2000);
  }
  //-----------------------------------------------------------------------------------------------------------------------------------------------
  if(turn == 4){
  angle_joint2_DO = 686+joint2_offset;   
  joint2_angle_DO_calculation();  
  joint_2_angle_DO_write ();    
  delay(2000);  
  base_angle_DO =542+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2000);
  joint_3.write(50);
  delay(1000);
  joint_4.write(60);
  delay(1000);
  joint_4.write(110);
  delay(1000);
  angle_joint2_DO = 634+joint2_offset;   
  joint2_angle_DO_calculation();  
  joint_2_angle_DO_write ();    
  delay(2000);
  angle_joint2_DO = 605+joint2_offset;   
  joint2_angle_DO_calculation();  
  joint_2_angle_DO_write ();    
  delay(2000);
  }
  //-----------------------------------------------------------------------------------------------------------------------------------------------

  gripper.write(40);
  delay(2000);
  angle_joint2_DO = 690+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
}
  //---------------------------------------------------------------------------------------------------------------------------------
void loop()
{ 
  
  if (Serial.available() > 0)  // wait for python Serial command
  {
  python = Serial.read(); // read serial
//---------------------------------------------------------------------------------------------------------------------------------
  
  if(python == '1')      // 1 pick      
  {
  turn = turn+1;  
  pick ();
  delay(2000);
  base_angle_DO =540+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2500);
  joint_3.write(40);
  delay(1000);   
  joint_4.write(25);
  delay(1000); 
  angle_joint2_DO = 630+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
  delay(2000);  
  gripper.write(180);
  delay(2000);    
  home_position ();  
  }

  //---------------------------------------------------------------------------------------------------------------------------------

  if(python == '2')      // 2 pick      
  {
  turn = turn+1;
  pick ();
  delay(2000);
  base_angle_DO =520+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2500);
  joint_3.write(60);
  delay(1000);   
  joint_4.write(30);
  delay(1000); 
  angle_joint2_DO = 618+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
  delay(2000);  
  gripper.write(180);
  delay(2000);    
  home_position ();  
  }

  //---------------------------------------------------------------------------------------------------------------------------------

  if(python == '3')      // 3 pick      
  {
  turn = turn+1;  
  pick ();
  delay(2000);
  base_angle_DO =515+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2500);
  joint_3.write(80);
  delay(1000);   
  joint_4.write(45);
  delay(1000); 
  angle_joint2_DO = 585+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
  delay(2000);  
  gripper.write(180);
  delay(1000);    
  home_position ();  
  }

  //----------------------------------------------------------------------------------------------------------------------------
  
  if(python == '4')      // 4 pick      
  {
  turn = turn+1;
  pick ();
  delay(2000);
  base_angle_DO =475+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2500);
  joint_3.write(20);
  delay(1000);   
  joint_4.write(40);
  delay(1000); 
  angle_joint2_DO = 648+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
  delay(2000);  
  gripper.write(180);
  delay(1000);    
  home_position ();  
  }

  //---------------------------------------------------------------------------------------------------------------------------------
  
  if(python == '5')      // 5 pick      
  {
  turn = turn+1;
  pick ();
  delay(2000);
  base_angle_DO =475+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2500);
  joint_3.write(20);
  delay(1000);
  joint_4.write(70);
  delay(1000);
  angle_joint2_DO = 653+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
  delay(2000);
  gripper.write(180);
  delay(1000);    
  home_position (); 
  
  }

  //----------------------------------------------------------------------------------------------------------------------------
  
  if(python == '6')      // 6 pick      
  {
  turn = turn+1;
  pick ();
  delay(2000);
  base_angle_DO =475+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2500);
  joint_3.write(80);
  delay(1000);
  joint_4.write(40);
  delay(1000);
  angle_joint2_DO = 605+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
  delay(2000);
  gripper.write(180);
  delay(1000);    
  home_position ();  

  }

  //---------------------------------------------------------------------------------------------------------------------------------
  
  if(python == '7')      // 7 pick      
  {
  turn = turn+1;
  pick ();
  delay(2000);
  base_angle_DO =380+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2500);
  joint_3.write(40);
  delay(1000);   
  joint_4.write(25);
  delay(1000);
  angle_joint2_DO = 620+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
  delay(2500);   
  gripper.write(180);
  delay(1000);    
  home_position ();  

  }
  //------------------------------------------------------------------------------------------------------------------------------
 
  if(python == '8')      // 8 pick      
  {
  turn = turn+1;
  pick ();
  delay(2000);
  base_angle_DO =408+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2500);
  joint_3.write(60);
  delay(1000);   
  joint_4.write(30);
  delay(1000);   
  angle_joint2_DO = 620+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
  delay(2000);
  gripper.write(180);
  delay(1000);    
  home_position ();  
  }
  //-----------------------------------------------------------------------------------------------------------------------------

  if(python == '9')      // 9 pick      
  {
  turn = turn+1;  
  pick ();
  delay(2000);
  base_angle_DO =424+base_offset;
  base_angle_DO_calculation ();     
  base_angle_DO_write ();           
  delay(2500);
  joint_3.write(80);
  delay(1000);   
  joint_4.write(50);
  delay(1000); 
  angle_joint2_DO = 607+joint2_offset;
  joint2_angle_DO_calculation();     
  joint_2_angle_DO_write (); 
  delay(2000);
  gripper.write(180);
  delay(1000);    
  home_position ();  
  }
  //---------------------------------------------------------------------------------------------------------------------------------
  if(python == '0')      // reset game
  {
  turn = 0 ;
  }
  //--------------------------------------------------------------------------------------------------------------------------------- 
  }
   
}


