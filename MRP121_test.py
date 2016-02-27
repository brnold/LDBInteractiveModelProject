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
# //  Primary coder                                     Bret
# //  Secondary coder                              Benjamin
# //  Code contributer                                Katrina
# //  Code contributer                                Ryan
# //***************************************************************************************************************** 
# //  Revision      
# //  0       Prototype code complete.                                                    Bret  2016-02-06
# //  1       Clean up  code.                                                             Bret  2016-02-12
# //  2       Add code for electrode tuning in case 0.                                    Bret  2016-02-14
# //  3       Add code new electrodes and time between samples.                           Bret  2016-02-15
# //
# //      
# //                     
# //  x       Final edits.                                                                TBD 2016-0x-xx
# //
# //*****************************************************************************************************************

import serbus, time

CHIP_ADDR      =      0x5A                      #Adafruit break out address.
LITTLE_ENDIAN    =    0                        # Integer formating.
BIG_ENDIAN      =     1                           # What I'm used to BH.



def I2CWriteBytes(data):
	bus.write( int(CHIP_ADDR), data) #yep, that's it. CHIP_ADDR is an int, data should be a list though

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

##############Program Starts Below#######
#Maybe I should make a main
bus = serbus.I2CDev(1)
bus.open()

try:
	while True:
		print
		print "Oh look, I'm doing something!"
		time.sleep(1)

except  KeyboardInterrupt:
	bus.close()
