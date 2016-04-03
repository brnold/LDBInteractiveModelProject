#************************************************************************************************************ 
#  ECE 491 Senior Design
#  Winter 2016
#  Team 6 
#
#  Python Script		: TouchObjs.py
#  Supporting Scripts	: ObjTouchCtrl.py,
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
#  0	Supporting script creation for touch sensing management.		Bret		2016-03-20
#                     
#  x	Edits.								TBD		2016-0x-xx
#
#************************************************************************************************************
import TouchCtrl
Status = 0
TOs =	[
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),	# net 0
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),	# net 1
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),	# net 2
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),	# net 3
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),	# net 4
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),	# net 5
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(),	# net 6
			TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj(), TouchCtrl.TouchObj()	# net 7
		]

StatusOfTOs =	[
					Status, Status, Status, Status,		# net 0
					Status, Status, Status, Status,		# net 1
					Status, Status, Status, Status,		# net 2
					Status, Status, Status, Status,		# net 3
					Status, Status, Status, Status,		# net 4
					Status, Status, Status, Status,		# net 5
					Status, Status, Status, Status,		# net 6
					Status, Status, Status, Status		# net 7
		]
def ConFigController():									# Configure every touch sensing IC
	idx = 0
	for idx in range (0,32):							# idx will range from 0 to 31
		TOs[idx].ConFigController()

def GetStatus():										# Update touch status from all ICs.
	idx = 0
	for idx in range (0,32):							# idx will range from 0 to 31
		StatusOfTOs[idx] = TOs[idx].displayStatus()			#This returns the Binary register value from the Chip.
#	print StatusOfTOs									# Feedback during development.
	return StatusOfTOs

def getTouchedElectrodes():
#Written by Benjamin on 3/3/2016
#Takes the value of the electroid status and converts it to a value
#NOT ROBUST YET, this will cause issues for anything on Subnet 0
	electroidStatus = ""
	electroidList = []
	EleBit  = 1
	for idx in range (0,32):							# idx will range from 0 to 31
		binStatus = TOs[idx].displayStatus()			#This returns the Binary register value from the Chip.
		for siX in range (0, 12):			# Build up touch status bit status
			if binStatus == None: # if the module is not enabled, break
				break
			c = binStatus & EleBit 
			if (c) >0:
			
				#electroidName = '%d%d%d' % ((idx/4),(idx%4), siX)
				
				#electroidName = hex(((idx/4)+255) + ((idx%4)+16) + siX)\
				electroidName = hex(((idx/4)*256) +((idx%4)*15)+siX)
				electroidList.extend([electroidName])  #add electroid number
		
			EleBit <<=1
	return electroidList	
# End of TouchObjs.py







