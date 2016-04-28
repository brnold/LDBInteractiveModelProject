#include <Wire.h>

#define TCAADDR 0x70

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
 
void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}
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


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin();
  //select the appropiate mux channel
  tcaselect(0);
  Wire.begin();
  I2CwriteBytes(ucSoftReset, sizeof(ucSoftReset));
  delay(1);
  I2CwriteBytes(ucThresh0_11, sizeof(ucThresh0_11));
  I2CwriteBytes(ucBaseLine, sizeof(ucBaseLine));
  I2CwriteBytes(ucDbCfg1_2, sizeof(ucDbCfg1_2));
}

void loop() {
  // put your main code here, to run repeatedly:
  UINT uiTouchStatus;
  tcaselect(0);
  Wire.begin();
  Wire.write()(&uiTouchStatus, 1, 0);                // Electrode touch status.
  Wire.end();
  Serial.print(uiTouchStatus);
  
  delay(100);

}
