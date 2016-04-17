#************************************************************************************************************ 
#  ECE 491 Senior Design
#  Winter 2016
#  Team 6 
#
#  Python Script		: I2C.py
#  Support Library		: serbus
#  Purpose: 
#  I2C communications script. TouchCtrl is the exclusive user of this module.
#
#  Functions: 
#		I2CWriteBytes():	- Writes a list of data to the selected  I2C Device.
#     
#		I2CReadStatus(): 	- Reads and combines to 8 bit status registers from an MPR121.
#  
#     
#  Primary coder														Benjamin
#  Secondary coder														Bret
#  Code contributor														Katrina
#  Code contributor														Ryan
#************************************************************************************************************ 
#  Revision      
#  0	 Supporting script creation for I2C communications.				Bret		2016-03-20
#                     
#  x	 Edits.															TBD			2016-0x-xx
#
#************************************************************************************************************
import serbus, time, os	
def I2CWriteBytes(CHIP_ADDR, data):
		bus.write(CHIP_ADDR, data)								# Write the list 'data' two the chip.

def I2CReadStatus(CHIP_ADDR):
#		print "Reading"											# Feedback during development.
		touchStatus = bus.readTransaction(CHIP_ADDR, 0, 2)		# Reading two 8 bit status registers.
#		print touchStatus										# Feedback during development.
		newStatus = touchStatus[0]+ 256*touchStatus[1]			# Combine to one number.
		return newStatus
def I2CRead1Byte(CHIP_ADDR, numb2read, regAddr):
#		print "Reading"											# Feedback during development.
		siNumb = numb2read + regAddr
		bytes1 = bus.readTransaction(CHIP_ADDR, 0, siNumb)		# Reading two 8 bit status registers.
		idx = 0
		newbytes1 = []
		for idx in range (0,numb2read):							# idx will range from 0 to 31
			siOff = idx+regAddr
			val = bytes1[siOff]
			newbytes1 += [val]							# Combine to one number.
		return newbytes1
def I2CRead2Byte(CHIP_ADDR, numb2read, regAddr):
#		print "Reading"											# Feedback during development.
#		print regAddr										# Feedback during development.
		siNumb = numb2read*2 + regAddr
#		print 'numb2read = %d, siNumb = %d' % (numb2read,siNumb)
		bytes2 = bus.readTransaction(CHIP_ADDR, 0, siNumb)		# Reading two 8 bit status registers.
#		bus.write(CHIP_ADDR, [4])								# Write the list 'data' two the chip.
#		time.sleep(0.01)											# Short delay.

#		bytes2 = bus.read(CHIP_ADDR, 12)		# Reading two 8 bit status registers.
		idx = 0
		newbytes2 = []
		for idx in range (0,numb2read):							# idx will range from 0 to 31
			siOffOne = 2*idx+regAddr
			siOffTwo = 2*idx+regAddr +1
			val = bytes2[siOffOne]
			val += 256*bytes2[siOffTwo]
			newbytes2 += [val]							# Combine to one number.
#			newbytes2[idx] += 256*bytes2[siOffTwo]			# Combine to one number.
#		print newbytes2										# Feedback during development.
#		print bytes2										# Feedback during development.
		return newbytes2

# Executes on import.
try:															# Required during development.
	print "bus object"											# Feedback during development.
	bus = serbus.I2CDev(1)										# Create a serbus.I2CDevice object.
	print "open"												# Feedback during development.
	bus.open()													# And open channel 1.
	print "I2C bus open"										# Feedback during development.

except IOError:													# Required during development.
			print "IO Error"									# Feedback during development.

