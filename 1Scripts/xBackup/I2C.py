import serbus, time, os			# pyglet
def I2CWriteBytes(CHIP_ADDR, data):
		bus.write(CHIP_ADDR, data) #
def I2CReadStatus(CHIP_ADDR):
#		print "Reading"
		touchStatus = bus.readTransaction(CHIP_ADDR, 0, 2)
#		print touchStatus
		newStatus = touchStatus[0]+ 256*touchStatus[1]
		return newStatus
try:
	print "bus object"
	bus = serbus.I2CDev(1)
	print "open"
	bus.open()
	print "I2C bus open"

except IOError:
			print "IO Error"

