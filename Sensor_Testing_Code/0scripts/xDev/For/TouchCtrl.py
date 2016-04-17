#************************************************************************************************************ 
#  ECE 491 Senior Design
#  Winter 2016
#  Team 6 
#
#  Python Script		: TouchCtrl.py
#  Supporting Scripts	: ModIC.py, NetsAddrs.py, Baselines.py, Thresholds.py,
#			  Globals.py, LocalCCs.py, LocalCDTs.py, and I2C.py
#
#  Purpose: 
#  Touch objects script. This python script module contains 32 objects of type TouchCtrl.TouchObj()
#  There are 4 touch objects (an address space of for 4 MPR121 IC chips) in
#  sub-network (an I2C channel) by 8 sub-networks (the number in I2C channels allowable by the
#  TCA9548A 1-to-8 I2C Multiplexer.
#
#  Functions: 
#		ConFigController(): - configure every MPR121 IC chip in the system.
#     
#		GetStatus(): 	   - Update the touch status of every touch object.
#  
#     
#  Primary coder														Benjamin
#  Secondary coder														Bret
#  Code contributor														Katrina
#  Code contributor														Ryan
#************************************************************************************************************ 
#  Revision      
#  0	 Supporting script creation for touch sensing management.		Bret		2016-03-20
#                     
#  x	 Edits.															TBD		2016-0x-xx
#
#************************************************************************************************************
import Thresholds, Baselines, Globals, LocalCDTs, LocalCCs, NetsAddrs, I2C, time, os
class TouchObj:
	'Common base class for all touch objects'
	Instance = 0
	subNet = 0
	SubNetBit = 1
	CHIP_ADDR		=	0x5A
	MUX_ADDR		=	0x70
	ucSoftReset		=	[0x80,0x63]	 # MPR121 Soft Reset
# This section need to be cleaned up. It works, but can be simplified.
	def __init__(self):
#		print TouchObj.__doc__
		self.Instance = TouchObj.Instance								# Set instance.
		self.ChipAddress	= TouchObj.CHIP_ADDR + TouchObj.Instance		# Set address
		self.SubNetBit		= TouchObj.SubNetBit							# fix setting 0x00 to 0x01		3-22-16 BH
		self.SubNet			= TouchObj.subNet								# Set decimal subnet.
		print	TouchObj.SubNetBit
		self.TouchStatus = 0
		if TouchObj.Instance < 3:
			TouchObj.Instance += 1											# Next instance.
		else:
			TouchObj.Instance = 0
			TouchObj.subNet += 1											# Next subnet.

	def ConFigController(self):												# Configuration function.
		if NetsAddrs.SubNetsEn[self.SubNet] == 1:							# SubNet must be Enabled.
			if NetsAddrs.EnabledAll[self.SubNet][self.Instance] == 1:		# Address must be Enabled.
				I2C.I2CWriteBytes(TouchObj.MUX_ADDR, [self.SubNetBit])		# Set Mux tosubnet.
				I2C.I2CWriteBytes(self.ChipAddress, TouchObj.ucSoftReset)	# Reset MPR121
				time.sleep(0.01)											# Short delay.
#				print Thresholds.ThresholdAll[self.SubNet][self.Instance]	# Confirmed!
																			# Thresholds to MPR121
				I2C.I2CWriteBytes(self.ChipAddress, Thresholds.ThresholdAll[self.SubNet][self.Instance])
																			# Thresholds to MPR121
				I2C.I2CWriteBytes(self.ChipAddress, LocalCDTs.LocalCDTAll[self.SubNet][self.Instance])
																			# Local Charge/Discharge times.
				I2C.I2CWriteBytes(self.ChipAddress, LocalCCs.LocalCCAll[self.SubNet][self.Instance])
																			# Local Charge/Discharge current.
				I2C.I2CWriteBytes(self.ChipAddress, Baselines.BaselineAll[self.SubNet][self.Instance])
																			# Global settings
				I2C.I2CWriteBytes(self.ChipAddress, Globals.GlobalAll[self.SubNet][self.Instance])

	def displayStatus(self):
		if NetsAddrs.SubNetsEn[self.SubNet] == 1:							# SubNet must be Enabled.
			if NetsAddrs.EnabledAll[self.SubNet][self.Instance] == 1:		# Address must be Enabled.
				I2C.I2CWriteBytes(TouchObj.MUX_ADDR, [self.SubNetBit])		# Confirmed correct!
				self.TouchStatus = I2C.I2CReadStatus(self.ChipAddress)		# Read touch status
				return self.TouchStatus
# End TouchCtrl.py