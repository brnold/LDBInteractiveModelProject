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
#  Touch control script. This python script defines and manages touch sensing objects.
#  An object represents one MPR121 IC chips. This script contains the function to setup the IC,
#  and read its touch status.
#
#  Functions: 
#		ConFigController(): - configure the MPR121 IC associated to a touch object.
#     
#		GetStatus(): 	   - Update the touch status associated to a touch object.
#  
#     
#  Primary coder														Benjamin
#  Secondary coder														Bret
#  Code contributor														Katrina
#  Code contributor														Ryan
#************************************************************************************************************ 
#  Revision      
#  0	Supporting script creation for touch sensing management.		Bret		2016-03-20
#  1	Corrected the SubNet MUX logic.									Bret		2016-03-22
#  2	Add performance data collection.								Bret		2016-03-28
#  3	Comment out performance data collection.						Bret		2016-04-23
#  4	Un-comment performance data collection.							Bret		2016-04-25
#
#************************************************************************************************************
import Thresholds, Baselines, Globals, LocalCDTs, LocalCCs, NetsAddrs, I2C, time, os
class TouchObj:
	'Common base class for all touch objects'
	Instance		=	0
	SubNet			=	0
	SubNetBit		=	1
	CHIP_ADDR		=	0x5A
	MUX_ADDR		=	0x70
	SoftReset		=	[0x80,0x63]	 # MPR121 Soft Reset
	def __init__(self):
#		print TouchObj.__doc__
		self.filtVal	=	[]												# Add filter input data.
		self.baseLines	=	[]												# Add baseline data.
		self.Instance = TouchObj.Instance									# Set instance.
		self.ChipAddress	= TouchObj.CHIP_ADDR + TouchObj.Instance		# Set address
		self.SubNetBit		= TouchObj.SubNetBit							# Mux channel
		self.SubNet			= TouchObj.SubNet								# Decimal subnet.
		self.TouchStatus	= 0
		if TouchObj.Instance < 3:
			TouchObj.Instance += 1											# Next instance.
		else:
			TouchObj.Instance = 0
			TouchObj.SubNet += 1											# Next subnet.
#			print	TouchObj.SubNetBit
			TouchObj.SubNetBit <<= 1										# Next channel

	def ConFigController(self):												# Configuration function.
		if NetsAddrs.SubNetsEn[self.SubNet] == 1:							# SubNet must be Enabled.
			if NetsAddrs.EnabledAll[self.SubNet][self.Instance] == 1:		# Address must be Enabled.
#********************************************************************************************************************
#* Comment the following line out if no MUX.
#********************************************************************************************************************
				I2C.I2CWriteBytes(TouchObj.MUX_ADDR, [self.SubNetBit])		# Set Mux tosubnet.
#********************************************************************************************************************
				I2C.I2CWriteBytes(self.ChipAddress, TouchObj.SoftReset)	# Reset MPR121
				time.sleep(0.05)											# Short delay.
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
		filtVal	= [0]
		if NetsAddrs.SubNetsEn[self.SubNet] == 1:							# SubNet must be Enabled.
			if NetsAddrs.EnabledAll[self.SubNet][self.Instance] == 1:		# Address must be Enabled.
#********************************************************************************************************************
#* Comment the following line out if no MUX.
				I2C.I2CWriteBytes(TouchObj.MUX_ADDR, [self.SubNetBit])		# Confirmed correct!
#********************************************************************************************************************
				self.TouchStatus = I2C.I2CReadStatus(self.ChipAddress)			# Read touch status
				self.filtVal = I2C.I2CRead2Byte(self.ChipAddress, 12, 0x04)		# Filtered input data.
				self.baseLines = I2C.I2CRead1Byte(self.ChipAddress, 12, 0x1e)	# Baseline data.
				for idx in range (0, 12):
					self.baseLines[idx] <<=2
#				print self.filtVal
				return self.TouchStatus
# End TouchCtrl.py
