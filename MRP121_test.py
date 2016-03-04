# -*- coding: utf-8 -*-
# /***************************************************************************************************************** 
# //  ECE 491 Senior Design
# //  Winter 2016
# //  Team 6 
# //  Proximity Capacitive Touch Sensor Controller and Electrode experimental verification software.  
# //    
# //  Purpose: 
# //  1) Verify that the MPR121 Cap Sense Controller is a valid solution for our project.
# //     
# //  2) Verify that all registers can be data can be read and written.  
# //     
# //  3) Configure MPR121 per experimental specifications for electorde sensitivity and reliability
# //     
# //  4) Transmit collected data for inclusion in the results report
# //     
# //    
# //  Current Micro-controller is the Arduino Uno.      
# //  
# //  Primary coder                                     Benjamin 
# //  Secondary coder                               Bret
# //  Code contributer                                Katrina
# //  Code contributer                                Ryan
# //***************************************************************************************************************** 
# //  Revision      
# //  0       Prototype code complete.                                                    Bret  2016-02-06
# //  1       Clean up  code.                                                             Bret  2016-02-12
# //  2       Add code for electrode tuning in case 0.                                    Bret  2016-02-14
# //  3       Add code new electrodes and time between samples.                           Bret  2016-02-15               
# //  4      Final edits to aruino code                                                              TBD 2016-0x-xx
# //  5       Began translation of logic to Python			Benjamin 2016-02-26
#
# //*****************************************************************************************************************

import serbus, time

CHIP_ADDR      =      0x5A                      #Adafruit break out address.
LITTLE_ENDIAN    =    0                        # Integer formating.
BIG_ENDIAN      =     1                           # What I'm used to BH.

###############################################################
##MRP121 Commands
ucSoftReset = [0x80,0x63] # MPR121 Soft Reset

#Baseline configuration settings
ucBaseLine = [0x2b,  # Data block starting address
                                              0x01,   # MHDR
                                              0x01,   # NHDR
                                              0x0e,   # NCLR
                                              0x00,   # FDLR
                                              0x01,   # MHDF
                                              0x05,   # NHDF
                                              0x01,   # NCLF
                                              0x09,   # FDLF
                                              0x00,   # NHDT
                                              0x00,   # NCLT
                                              0x00]  # FDLT

#Configuration settings
ucDbCfg1_2 = [0x5b,   # Data block starting address    
                            0x00,   # Debounce, Touch(b6, b5, b4) 
                                                      #and Release(b2, b1, b0) register setting.
                                              0x07,   # Filter (b7,b6 - 00 = 6 samples)
                                                      # and Global CDC (b5,b4,b3,b2,b1,b0) 000111= 7uA
                                              0x93,   #Global CDT (b7,b6,b5,) 4us
                                                      # SFI - 2nd filter (b4,b3) 10= 6 sample 
                                                       # ESI (b2,b1,b0) 011 = 8ms sample interval.
                                              0x89] # ECR - CL (b7,b6) 0 = default baseline tracking
                                                      # ELEPROX_EN (b5,b4) 0 = proximity disabled
                                                      # ELE_EN (b3,b2,b1,b0) 2 = ELE0 ~ ELE8 enabled.

#MRP121 - threasholds
ucThresh0_11  = [0x41,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,
                                                      0x38,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06]

#This function takes a list of 
def  listHextToInt(theList):
	for hexNum in theList:
		intList.append( int(hexNum))
	return intList                                      

def I2CWriteBytes(data):
	bus.write( CHIP_ADDR, data) #yep, that's it. CHIP_ADDR is an int, data should be a list though

# I2CRead2Bytes
# Use bus.readTransaction instead
#---------------------
# readTransaction(slave_addr, tx_byte, n_bytes)
# Parameters:	
# slave_addr (int) – The address of the slave to read from
# tx_byte (int) – The byte to write before reading
# n_bytes (int) – The number of bytes to read
# Returns:	
# A list of ints of the bytes read

# Writes tx_byte then immediately reads n_bytes bytes from the I2C slave device with the given address and returns them as a list. This is useful for things like reading register values from memory mapped devices.

##############Program Starts Below##################################
#Maybe I should make a main

try:
	bus = serbus.I2CDev(1)
	bus.open()

	print "IIC bus open"

	I2CWriteBytes(ucSoftReset)
	time.sleep(0.01) # the time.sleep taked floats and evaluvates in seconds
	I2CWriteBytes( ucThresh0_11)
	I2CWriteBytes(ucBaseLine)
	I2CWriteBytes(ucDbCfg1_2)


	while True:
		print
		print "Oh look, I'm doing something!"
		time.sleep(1)

except IOError:
      print "Really, an IO error"

except  KeyboardInterrupt:
	bus.close()
