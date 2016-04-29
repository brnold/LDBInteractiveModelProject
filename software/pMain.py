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
from bbio import *
import TouchCtrl, TouchObjs, soundFunctions, I2C

tSinceLastTouch = -5 # set the time to somthing so it will play the first touch immedetly

#setup the switch
pinMode( GPIO1_28, OUTPUT)
digitalWrite( GPIO1_28, LOW) #turn on the sensors
time.sleep(0.2)

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


		#print "Now getting the electrode status"
		electroidList = TouchObjs.getTouchedElectrodes()
		for idx in range (0, len(electroidList)):
			print electroidList[idx]
		
		#first, check and see if the I2C error counter is larger than some value

		if(I2C.error_counter > 0):
			if(I2C.error_counter > 2):
				raise SystemExit
			else:
				I2C.error_counter = I2C.error_counter - 1
				
		if(len(electroidList)>0):

			#see time since last touch,
			# if time is grater thatn 5 or so muniues, play the welcome


			if((time.time()- tSinceLastTouch) > 60*5):
				os.system('mpg321  ~/software/audio/INTRO.mp3')
				tSinceLastTouch = time.time()
			elif(len(electroidList) > 3):
				os.system('mpg321  ~/software/audio/MultipleTouch.mp3')
				tSinceLastTouch = time.time()
			elif((len(electroidList) <= 3) ):
				soundFunctions.playSoundFromElectrode(electroidList[0])
				tSinceLastTouch = time.time()

		#Now for some incredibly briliant software 

		#
		# electroidList = TouchObjs.getTouchedElectrodes()

		# room.updateRoomList(electroidList)
		# room.removeExpiredRooms() # get rid of all the old unplayed rooms
		# room.removeNonTouchedRooms(electroidList)
		# numUnplayedRooms = room.getNumberUnplayedRooms()

		# if numUnplayedRooms == 1: #best case
		# 	#naiave way of doing this
		# 	room.playFirstUnplayedRoom()
		


#************************************************************************************************************
		time.sleep(0.2)
except KeyboardInterrupt:							# Required during development.
	print ""
	print "Kennel Model Stopped!"					# Feedback during development.
	digitalWrite( GPIO1_28, HIGH) #turn off the sensors

except SystemExit:
	print "SystemExit exception Raised"
	print "This happened becuase there was an IIC error"
	digitalWrite(GPIO1_28, HIGH)

# End of pMain.py

