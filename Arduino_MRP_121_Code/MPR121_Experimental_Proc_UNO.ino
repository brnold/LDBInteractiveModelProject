//***************************************************************************************************************** 
//  ECE 491 Senior Design
//  Winter 2016
//  Team 6 
//  Proximity Capacitive Touch Sensor Controller and Electrode experimental verification software.  
//    
//  Purpose: 
//  1) Verify that the MPR121 Cap Sense Controller is a valid solution for our project.
//     
//  2) Verify that all registers can be data can be read and written.  
//     
//  3) Configure MPR121 per experimental specifications for electorde sensitivity and reliability
//     
//  4) Transmit collected data for inclusion in the results report
//     
//    
//  Current Micro-controller is the Arduino Uno.      
//  
//  Primary coder                                     Bret
//  Secondary coder                              Benjamin
//  Code contributer                                Katrina
//  Code contributer                                Ryan
//***************************************************************************************************************** 
//  Revision      
//  0       Prototype code complete.                                                    Bret  2016-02-06
//  1       Clean up  code.                                                             Bret  2016-02-12
//  2       Add code for electrode tuning in case 0.                                    Bret  2016-02-14
//  3       Add code new electrodes and time between samples.                           Bret  2016-02-15
//
//      
//                     
//  x       Final edits.                                                                TBD 2016-0x-xx
//
//*****************************************************************************************************************
#include <Wire.h>
//*****************************************************************************************************************
// Define and initialize global variables.
//***************************************************************************************************************** 
// Pin 13 has an LED connected on most Arduino boards.
#define CHIP_ADDR           0x5A                      // Adafruit break out address.
#define LITTLE_ENDIAN        0                        // Integer formating.
#define BIG_ENDIAN           1                        // What I'm used to BH.
#define UCHAR               unsigned char
#define UINT                unsigned int

            int             led = 13;
            int             siState = 1;
            int             siXaxis,siYaxis,siZaxis;
unsigned    int             uiGs, uiTemp;
unsigned    int             uiIntRegArray[10];
            int             siKeyInputVal=0;
            int             siEndian = 0;
UINT                        uiNumbElectEnab = 0;      // Use a variable to keep track of electrode count.
UINT                        uiStartElectNumb = 0;      // Use a variable to keep track of electrode count.
UCHAR                       ucSoftReset[2] = {0x80,0x63}; // MPR121 Soft Reset
// Baseline configuration settings
UCHAR                       ucBaseLine[12] = {0x2b,   // Data block starting address
                                              0x01,   // MHDR
                                              0x01,   // NHDR
                                              0x0e,   // NCLR
                                              0x00,   // FDLR
                                              0x01,   // MHDF
                                              0x05,   // NHDF
                                              0x01,   // NCLF
                                              0x09,   // FDLF
                                              0x00,   // NHDT
                                              0x00,   // NCLT
                                              0x00};  // FDLT
//UCHAR                   ucDbCfg1_2[5]  = {0x5b,0x00,0x10,0x20,0x8f}; // MPR121 - debounce, CDC, CDT,Elect Config
// Configuration settings
UCHAR                       ucDbCfg1_2[5]  = {0x5b,   // Data block starting address    
                                              0x00,   // Debounce, Touch(b6, b5, b4) 
                                                      // and Release(b2, b1, b0) register setting.
                                              0x07,   // Filter (b7,b6 - 00 = 6 samples)
                                                      // and Global CDC (b5,b4,b3,b2,b1,b0) 000111= 7uA
                                              0x93,   // Global CDT (b7,b6,b5,) 4us
                                                      // SFI - 2nd filter (b4,b3) 10= 6 sample 
                                                      // ESI (b2,b1,b0) 011 = 8ms sample interval.
                                              0x89};  // ECR - CL (b7,b6) 0 = default baseline tracking
                                                      // ELEPROX_EN (b5,b4) 0 = proximity disabled
                                                      // ELE_EN (b3,b2,b1,b0) 2 = ELE0 ~ ELE8 enabled.
                                                      
                                                      // MPR121 - thresholds
UCHAR                       ucThresh0_11[25]  = {0x41,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,
                                                      0x38,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06}; 
UCHAR                       ucRegData[130];           // MPR121 read back register data.               
unsigned    char            ucXlsb;
unsigned    char            scXmsb;
unsigned    int             uiCounter = 0;
            char            scString[500];
            char            scTemp = 0x08;
unsigned    long            ulTime, ulLastTime;                           // Timing Variables.

//*****************************************************************************************************************
// the setup routine runs once when you press reset:
//*****************************************************************************************************************
void setup()
{                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);                                // LED on.
//  Serial.begin(9600);
  Serial.begin(38400);
  siEndian = LITTLE_ENDIAN;                               // MPR121 is Littel Endian format;
  Wire.begin();
  I2CwriteBytes(ucSoftReset, sizeof(ucSoftReset));
  delay(1);
  I2CwriteBytes(ucThresh0_11, sizeof(ucThresh0_11));
  I2CwriteBytes(ucBaseLine, sizeof(ucBaseLine));
  I2CwriteBytes(ucDbCfg1_2, sizeof(ucDbCfg1_2));
  ulTime = micros();                                      // Initialize time variables.
  ulLastTime = ulTime;
  uiNumbElectEnab =   ucDbCfg1_2[4]&0x0f;                 // ECR electrode enabled field.
  uiStartElectNumb =0x0f;
}

//*****************************************************************************************************************
// the loop routine runs over and over again forever:
//*****************************************************************************************************************
void loop()
{
  UINT uiIdx,uiTouchStatus,uiTouchMask=1;  
  digitalWrite(led, LOW);                           // turn the LED on (HIGH is the voltage level)
  switch (siState) 
  {
 case 0:
      //***********************************************************************************************************
      // case 0;
      // Electrode touch, filter, and baseline data tunning.
      //                                                                              b.henson  2016-02-14
      //***********************************************************************************************************
      ulTime = micros();                                  // Get the current time.
      I2Cread2Bytes(&uiTouchStatus, 1, 0);                // Electrode touch status.
//      sprintf (scString, "TS:\t%4.4X\t", uiIntRegArray[0]);
//      Serial.print(scString);
      for (uiIdx=0;uiIdx<uiNumbElectEnab;uiIdx++)         // Read all of the electrode data.
      {
        I2Cread2Bytes(&uiIntRegArray[uiIdx], 1, (2*uiIdx+0x04));
        I2Cread1Byte(&ucRegData[uiIdx], 1, uiIdx+0x1e);
       }
      sprintf (scString, "Filter, BaseLine, Touch:\t");   // Input A/D counts out from filter 2.
      Serial.print(scString);
      Serial.print((ulTime-ulLastTime));                  // calculate time since last sample
      ulLastTime = ulTime;                                // Reset the last time reference value 
      Serial.print("\t");
      for (uiIdx=0;uiIdx<uiNumbElectEnab;uiIdx++)         // Format and write the electrode status.
      {
        uiTemp = (ucRegData[uiIdx]<<2);
        if (uiTouchStatus&uiTouchMask)
          sprintf (scString, "ELE%d\t%5.0d\t%5.0d\t1\t", uiIdx, uiIntRegArray[uiIdx], uiTemp);
        else
         sprintf (scString, "ELE%d\t%5.0d\t%5.0d\t0\t", uiIdx, uiIntRegArray[uiIdx], uiTemp);
         if ((uiStartElectNumb == 0x0f) || (uiStartElectNumb == uiIdx))
         Serial.print(scString);
         uiTouchMask = (uiTouchMask<<1);
         delay(10);// makes ELE4 baseline stop flashing to zero - serial data to monitor issue.
       }
     Serial.println("");
      break;
  case 1:   
      //***********************************************************************************************************
      // case 1;
      // Write one text line for Excel Filtering, and then change state to 0 for electrode data collection.
      //                                                                              b.henson  2016-02-14
      //***********************************************************************************************************
        Serial.print("\tSample Time\t");
        for (uiIdx=0;uiIdx<uiNumbElectEnab;uiIdx++)
          {
            sprintf(scString,"Electrode %d\tFilter\tBaseLine\tTouch:\t", uiIdx);        
            Serial.print(scString);
          }
        Serial.println("");
        siState=0;
      break;
    case '0': 
      //***********************************************************************************************************
      // case '0';
      // TBD
      //                                                                              b.henson  2016-02-xx
      //***********************************************************************************************************
          uiStartElectNumb = 0;
        
//      I2Cread1Byte(&ucRegData[0], 1, 0x5d);               // debugging
//      for (int siIx=0;siIx<1;siIx++)
//      {
//        sprintf (scString, " %2X,", ucRegData[siIx]);
//        Serial.print(scString);
//      }
    //  Serial.println("Case 0x30");
//      Serial.println(ucRegData[0]);
      siState=0;                                         // This state value will be picked up by default.
      break;
    case '1': 
      //***********************************************************************************************************
      // case '1';
      // TBD
      //                                                                              b.henson  2016-02-xx
      //***********************************************************************************************************
        if ((ucDbCfg1_2[4]&0x0f)>1)
          uiStartElectNumb = 1;
      siState=0;                                         // This state value will be picked up by default.
      break;
    case '2': 
      Serial.println("Case 0x31");
        if ((ucDbCfg1_2[4]&0x0f)>2)
          uiStartElectNumb = 2;
      siState=0;                                         // This state value will be picked up by default.
      break;
    case '3': 
        if ((ucDbCfg1_2[4]&0x0f)>3)
          uiStartElectNumb = 3;
      siState=0;                                         // This state value will be picked up by default.
      break;
    case '4': 
        if ((ucDbCfg1_2[4]&0x0f)>4)
          uiStartElectNumb = 4;
      siState=0;                                         // This state value will be picked up by default.
      break;
    case '5': 
        if ((ucDbCfg1_2[4]&0x0f)>5)
          uiStartElectNumb = 5;
      siState=0;                                         // This state value will be picked up by default.
      break;
    case '6': 
        if ((ucDbCfg1_2[4]&0x0f)>6)
          uiStartElectNumb = 6;
      siState=0;                                         // This state value will be picked up by default.
      break;
    case '7': 
        if ((ucDbCfg1_2[4]&0x0f)>7)
          uiStartElectNumb = 7;
      siState=0;                                         // This state value will be picked up by default.
      break;
    case '8': 
        if ((ucDbCfg1_2[4]&0x0f)>8)
          uiStartElectNumb = 8;
      siState=0;                                         // This state value will be picked up by default.
      break;
    efault:
      //***********************************************************************************************************
      // default;
      // Pick up undefined state values and do nothing!
      //                                                                              b.henson  2016-02-06
      //***********************************************************************************************************
      break;
  }

  delay(90);                                             // Sample time main control.
  siKeyInputVal=Serial.read();
  if (siKeyInputVal>=0x30 && siKeyInputVal<=0x39)         // key 0 or 1.
  {
//    siState = (siKeyInputVal - 0x30);
    siState = siKeyInputVal;
  }
//  Serial.println(siState);                              // Debugging.
} // End of loop()
//*****************************************************************************************************************
//* 
//* I2C - Read unsigned char(s) from regesters.
//* 
//* Inputs
//*   ucRegArray      - an unsigned char pointer to the receiving data array.
//*   siNumbReg2Read  - int value of sequential reads to be performed.
//*   ucRegAddr       - unsigned char for the beginning register address.
//*                                                                                     b.henson 2016-02-06
//***************************************************************************************************************** 
void I2Cread1Byte(unsigned char *ucRegArray, int siNumbReg2Read, UCHAR ucRegAddr)
{
  Wire.beginTransmission(CHIP_ADDR);                      // Setup to transmit the register to the selet device.
  Wire.write(ucRegAddr);                                  // Que the callers regester address.
//  Serial.println(ucRegAddr);                            // Send the address to the select device.
  Wire.endTransmission(false);
  while (Wire.requestFrom(CHIP_ADDR, siNumbReg2Read)
          != siNumbReg2Read);                             // Read bytes from slave.
  for (int siX=0;siX<siNumbReg2Read;siX++)                // Transfer data bytes to callers array.
  {
    ucRegArray[siX] = Wire.read();
//    Serial.println(ucRegArray[siX]);                    // Debugging.
  }
} // End I2Cread1Byte(
//*****************************************************************************************************************
// 
//* I2C - Read unsigned integer(s)from regesters.
//* 
//* Inputs
//*   uiRegArray      - an unsigned char pointer to the receiving data array.
//*   siNumbReg2Read  - int value of sequential reads to be performed.
//*   ucRegAddr       - unsigned char for the beginning register address.
//* 
//*                                                                                     b.henson 2016-02-06
//***************************************************************************************************************** 
void I2Cread2Bytes(unsigned int *uiRegArray, int siNumbReg2Read, UCHAR ucRegAddr)
{
  Wire.beginTransmission(CHIP_ADDR);                      // Setup to transmit the register to the selet device.
  Wire.write(ucRegAddr);                                  // Que the callers regester address.
  Wire.endTransmission(false);                            // Send the address to the select device.
//  Serial.println(ucRegAddr);                            // Debugging.
  while (Wire.requestFrom(CHIP_ADDR, (siNumbReg2Read*2))
          != (siNumbReg2Read*2));                         // Read bytes from slave.
//  Serial.println((siNumbReg2Read*2));                   // Debugging.
  for (int siX=0;siX<siNumbReg2Read;siX++)                // Transfer data bytes to callers array.
  {
    if (siEndian == BIG_ENDIAN)                           // Endianness check.
      uiRegArray[siX] = ((Wire.read()<<8)+Wire.read());   // Without the outter parenthesis, the program breaks.
    else
      uiRegArray[siX] = (Wire.read()+(Wire.read()<<8));   // Without the outter parenthesis, the program breaks.
  }
} // End I2Cread2Bytes(
//*****************************************************************************************************************
//* 
//* I2C - Write unsigned char(s) to regester(s).
//* 
//* Inputs
//*   ucWriteArray    - an unsigned char pointer to the receiving data array.
//*   siNumbReg2Write - int value of sequential reads to be performed.
//*  
//*                                                                                     b.henson 2016-02-06
//***************************************************************************************************************** 
void I2CwriteBytes(unsigned char *ucWriteArray, int siNumbReg2Write)
{
  Wire.beginTransmission(CHIP_ADDR);                      // Setup to transmit the register to the selet device.
  Wire.write(ucWriteArray, siNumbReg2Write);              // The callers formatted array contains everything needed.
  Wire.endTransmission();                                 // 
} // End I2CwriteBytes(

