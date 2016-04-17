import serbus, time, os			# pyglet
# Import PyBBIO library:
from bbio import *
CHIP_ADDR		=	0x5A
LITTLE_ENDIAN	=	0                        # Integer formating.
BIG_ENDIAN		=	1                        # What I'm used to, BH.


ucSoftReset	= [0x80,0x63]	 # MPR121 Soft Reset
# Baseline configuration settings.
ucBaseLine	=	[	0x2b,   # Data block starting address
					0x04,   # MHDR
					0x01,   # NHDR
					0x0e,   # NCLR
					0x00,   # FDLR
					0x01,   # MHDF
					0x05,   # NHDF
					0x01,   # NCLF
					0x0e,   # FDLF
					0x00,   # NHDT
					0x00,   # NCLT
					0x00];  # FDLT

# Global configuration settings
ucGlobalSettings	=	[	0x5b,   # Data block starting address    
                            0x00,   # Debounce, Touch(b6, b5, b4) 
                                    # and Release(b2, b1, b0) register setting.
                            0x07,   # Filter (b7,b6 - 00 = 6 samples)
                                    # and Global CDC (b5,b4,b3,b2,b1,b0) 000111= 7uA
                            0x93,   # Global CDT (b7,b6,b5,) 4us
                                    # SFI - 2nd filter (b4,b3) 10= 6 sample 
                                    # ESI (b2,b1,b0) 011 = 8ms sample interval.
                            0x89];  # ECR - CL (b7,b6) 0 = default baseline tracking
                                    # ELEPROX_EN (b5,b4) 0 = proximity disabled
                                    # ELE_EN (b3,b2,b1,b0) 2 = ELE0 ~ ELE8 enabled.
                                                      
# MPR121 - thresholds
ucThresh0_11		=	[	0x41,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,
							0x10,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06,0x0c,0x06
						] 
									# ELE6 Touch Threshold changed from 0x0c to 0x38.
ucELE0_11cdt	=	[	0x6c,0x00,0x00,0x00,0x00,0x00,0x00] 
                                                      # 0 = Use Global CDT.
ucELE0_11cc		=	[	0x5F,0x00,0x00,0x00,0x0b,0x00,0x00,
						0x07,0x00,0x00,0x00,0x00,0x00
					] 
									# ELE6 charge current = 9 uA.

pot1 = AIN0 # pin 39 on header P9 
pot2 = AIN2 # pin 37 on header P9 

def setup():
  # Nothing to do here
  pass

def	listHexToInt(theList):
		for hexNum in theList:
			intList.append(int(hexNuM))
		return intList

def I2CWriteBytes(data):
		bus.write(CHIP_ADDR, data) #

touchStatus = [0x00, 0x00]
i=0
try:
	print "bus object"
	bus = serbus.I2CDev(1)
	print "open"
	bus.open()
	print "I2C bus open"
	I2CWriteBytes(ucSoftReset)
	time.sleep(0.01)
	I2CWriteBytes(ucThresh0_11)
	I2CWriteBytes(ucELE0_11cdt)
	I2CWriteBytes(ucELE0_11cc)
	I2CWriteBytes(ucBaseLine)
	I2CWriteBytes(ucGlobalSettings)
	touchStatus = bus.readTransaction(CHIP_ADDR, 0, 2)
	print touchStatus[0] + touchStatus[1]
	while 1==1:
		# Get the ADC values:
		val1 = analogRead(pot1)
		val2 = analogRead(pot2)
		# And convert to voltages:
		voltage1 = inVolts(val1)
		voltage2 = inVolts(val2)
		print " pot1 ADC value: %i - voltage: %fv" % (val1, voltage1)
		print " pot2 ADC value: %i - voltage: %fv\n" % (val2, voltage2)
		touchStatus = bus.readTransaction(CHIP_ADDR, 0, 2)

	#			print touchStatus[0] + touchStatus[1]
		if touchStatus[0] == 1:
			print "Electrode 0 was touched"
		elif  touchStatus[0] == 2:
			print "Electrode 1 was touched"
		elif  touchStatus[0] == 4:
			print "Electrode 2 was touched"
		elif  touchStatus[0] == 8:
			print "Electrode 3 was touched"
		elif  touchStatus[0] == 16:
			print "Electrode 4 was touched"
		elif  touchStatus[0] == 32:
			print "Electrode 5 was touched"
		elif  touchStatus[0] == 64:
			print "Electrode 6 was touched"
		elif  touchStatus[0] == 128:
			print "Electrode 7 was touched"
		elif  touchStatus[1] == 1:
			print "Electrode 8 was touched"
		else:
			print "No touch"
		time.sleep(0.5)

except IOError:
			print "IO Error"
except KeyboardInterrupt:
			print "Keyboard"

