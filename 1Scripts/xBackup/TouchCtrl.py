import Thresholds, Baselines, Globals, LocalCDTs, LocalCCs, NetsAddrs, I2C, time, os

class TouchObj:
	'Common base class for all touch objects'
	count = 0
	subNet = 0
	CHIP_ADDR		=	0x5A
	MUX_ADDR		=	0x70
	LITTLE_ENDIAN	=	0                        # Integer formating.
	BIG_ENDIAN		=	1                        # What I'm used to, BH.
	ucSoftReset	= [0x80,0x63]	 # MPR121 Soft Reset
	SetChannel	= [0x20]	 # MPR121 Soft Reset
	ucELE0_11cdt	=	[	0x6c,0x00,0x00,0x00,0x00,0x00,0x00] 
                                                      # 0 = Use Global CDT.
	ucELE0_11cc		=	[	0x5F,0x00,0x00,0x00,0x0b,0x00,0x00,
						0x07,0x00,0x00,0x00,0x00,0x00
					] 
									# ELE6 charge current = 9 uA.
	def __init__(self):
#		print TouchObj.__doc__
		self.instance = TouchObj.count
		self.ChipAddress = TouchObj.CHIP_ADDR + TouchObj.count
		if TouchObj.subNet == 0:
			self.SubNetD = 0x00
		elif TouchObj.subNet == 1:
			self.SubNetD = 0x01
		elif TouchObj.subNet == 2:
			self.SubNetD = 0x04
		elif TouchObj.subNet == 3:
			self.SubNetD = 0x08
		elif TouchObj.subNet == 4:
			self.SubNetD = 0x10
		elif TouchObj.subNet == 5:
			self.SubNetD = 0x20
		elif TouchObj.subNet == 6:
			self.SubNetD = 0x40
		else:
			self.SubNetD = 0x80
		self.SubNet = TouchObj.subNet
		self.TouchStatus = 0
		if TouchObj.count < 3:
			TouchObj.count += 1
		else:
			TouchObj.count = 0
			TouchObj.subNet += 1

	def ConFigController(self):
		if NetsAddrs.SubNetsEn[self.SubNet] == 1:
			if NetsAddrs.EnabledAll[self.SubNet][self.instance] == 1:
#				print "Instance %d SubNet %d SubNetD %X  ChipSddress %X" % (self.instance, self.SubNet, self.SubNetD, self.ChipAddress)
				I2C.I2CWriteBytes(TouchObj.MUX_ADDR, [self.SubNetD])
				I2C.I2CWriteBytes(self.ChipAddress, TouchObj.ucSoftReset)
				time.sleep(0.01)
#				print Thresholds.ThresholdAll[self.SubNet][self.instance] # Confirmed!
				I2C.I2CWriteBytes(self.ChipAddress, Thresholds.ThresholdAll[self.SubNet][self.instance])
				I2C.I2CWriteBytes(self.ChipAddress, LocalCDTs.LocalCDTAll[self.SubNet][self.instance])
				I2C.I2CWriteBytes(self.ChipAddress, LocalCCs.LocalCCAll[self.SubNet][self.instance])
				I2C.I2CWriteBytes(self.ChipAddress, Baselines.BaselineAll[self.SubNet][self.instance])
				I2C.I2CWriteBytes(self.ChipAddress, Globals.GlobalAll[self.SubNet][self.instance])
	def displayStatus(self):
		if NetsAddrs.SubNetsEn[self.SubNet] == 1:
			if NetsAddrs.EnabledAll[self.SubNet][self.instance] == 1:
#				print "Instance %d SubNet %d SubNetD %X  ChipSddress %X" % (self.instance, self.SubNet, self.SubNetD, self.ChipAddress)
				I2C.I2CWriteBytes(TouchObj.MUX_ADDR, [self.SubNetD])		# Confirmed correct.
				self.TouchStatus = I2C.I2CReadStatus(self.ChipAddress)
				return self.TouchStatus
		

