#************************************************************************************************************ 
#  ECE 491 Senior Design
#  Winter 2016
#  Team 6 
#  Leader Dog for the Blind Interactive Kennel facility model.  
#  Main line for capacitive touch sensing and control.  
#    
#  Python Script		: pMain.py
#  Supporting Scripts	: ModIC.py, TouchObjs.py, ObjTouchCtrl.py,
#						  NetsAddrs.py, Baselines.py, Thresholds.py,
#						  Globals.py, LocalCCs.py, LocalCDTs.py, and I2C.py
#
#  Hardware Platform	: BeagleBone Black, a single-board computer running Angstrom Linux.
#
#  Purpose: 
#  1) On power up, configure all of the Capacitive Touch Sensor Controllers.
#     
#  2) Check IR sensor for client presents.  
#     
#  3) Enable/Disable Electrodes when client present/not present.
#     
#  4) Read sensor touch status and decode current touch location or no touch condition.
#     
#  5) Play the script for the currently touched location.
#     
#	This python script is based on the experimental procedure used to test the MPR121, and verify
#	its ability to satisfy our touch sensing requirements.
#	Sketch name:	MPR121_Experimental_Proc_UNO.ino
#  
#  Primary coder											Benjamin
#  Secondary coder											Bret
#  Code contributor											Katrina
#  Code contributor											Ryan
#************************************************************************************************************ 
#  Revision      
#  0	Prototype python script completed.					Benjamin		2016-03-06
#  1	Defined and verify model python script.				Bret			2016-03-20
#                     
#  x	Edits.												TBD				2016-0x-xx
#
#************************************************************************************************************
import time, os, sys
import TouchCtrl, TouchObjs, soundFunctions

roomList = [None]

def updateRoomList(electroidList):
	global roomList
	for idx in range(0, len(electroidList)):
		new_list = [x for x in myList if x.age == 30] #check and see if we allready have the object.
		if(len(new_list)==0) #k, add the object
			roomList.append(electroidList[idx])

print "Kennel Model Running!"						# Feedback during development.
TouchObjs.ConFigController()						# Configure the touch objects.
#************************************************************************************************************
# The one, and only, never ending processing loop.
#************************************************************************************************************
try:												# Required durring development.
	while 1==1:
#************************************************************************************************************
# Under construction! 
# IR Sensor status check goes here in the next revision.
# This section gets replaced by audio narrative processing in the next revision.
#
		# print "--------------OLD WAY--------------------"
		# TouchStatus = TouchObjs.GetStatus()			# Call the get status function.
		# for idx in range (0, 32):
		# 	if TouchStatus[idx] > 0:
		# 		print TouchStatus[idx]
		# print "-------------NOW MY WONDERFUL NEW FUNCITON-----------------"
		electroidList = TouchObjs.getTouchedElectrodes()
		for idx in range (0, len(electroidList)):
			print electroidList[idx]
		

		if(len(electroidList) > 1):
			os.system('mpg321 ./audio/MultipleTouch.mp3')
		elif(len(electroidList) == 1):
			soundFunctions.playSoundFromElectrode(electroidList[0])
#************************************************************************************************************
		time.sleep(0.5)
except KeyboardInterrupt:							# Required during development.
	print ""
	print "Kennel Model Stopped!"					# Feedback during development.

# End of pMain.py

