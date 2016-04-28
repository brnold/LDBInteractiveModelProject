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
#  1	Add performance data collection.								Bret		2016-03-28
#  2	Comment out performance data collection.						Bret		2016-04-23
#  3	Un-comment performance data collection.							Bret		2016-04-25
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
FiltValsOfTOs =		[[],[],[],[],[],[],[],[],			# 32 filtered input sets.
					 [],[],[],[],[],[],[],[],
					 [],[],[],[],[],[],[],[],
					 [],[],[],[],[],[],[],[]
					]
BaseLineValsOfTOs =	[[],[],[],[],[],[],[],[],			# 32 baseline data sets.
					 [],[],[],[],[],[],[],[],
					 [],[],[],[],[],[],[],[],
					 [],[],[],[],[],[],[],[]
					]
def ConFigController():									# Configure every touch sensing IC
	idx = 0
	for idx in range (0,32):							# idx will range from 0 to 31
		TOs[idx].ConFigController()

def GetStatus():										# Update touch status from all ICs.
	idx = 0
	for idx in range (0,32):							# idx will range from 0 to 31
		StatusOfTOs[idx] = TOs[idx].displayStatus()
		FiltValsOfTOs[idx] = TOs[idx].filtVal			# Add filter input collection.
		BaseLineValsOfTOs[idx] = TOs[idx].baseLines		# Add baseline data collection.
	return StatusOfTOs
# End of TouchObjs.py
