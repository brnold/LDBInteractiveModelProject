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
#  2	Add performance data collection.					Bret			2016-03-28
#                     
#  x	Edits.												TBD				2016-0x-xx
#
#************************************************************************************************************
import time, os, sys
import TouchCtrl, TouchObjs

print "Kennel Model Running!"						# Feedback during development.
TouchObjs.ConFigController()						# Configure the touch objects.
#************************************************************************************************************
# The one, and only, never ending processing loop.
#************************************************************************************************************
try:												# Required durring development.
	os.system('clear')
	while 1==1:
#************************************************************************************************************
# Under construction! 
# IR Sensor status check goes here in the next revision.
# This section gets replaced by audio narrative processing in the next revision.
#
		TouchStatus = TouchObjs.GetStatus()			# Call the get status function.
		EleBit		=	1
		siX = 0
		siStatTmp = 0
		iLst1=[]
		for idx in range (0, 32):
			if (idx) == 8:
#			if TouchObjs.StatusOfTOs[idx] > 0:
#			if TouchStatus[idx] > 0:
				siStatTmp = TouchObjs.StatusOfTOs[idx]
				for siX in range (0, 12):					# Build up touch status bit status
					if siStatTmp == None:
						siStatTmp = 0
					c = siStatTmp & EleBit
					if (c) >0:
						iLst1 += [1]
					else:
						iLst1 += [0]
					EleBit <<=1
#				print 'SubNet = %d\t%3.0X' % (idx/4, TouchObjs.StatusOfTOs[idx])
				myString = ''
				for siX in range (0, 12):
#					myString +='%d\t' % (iLst1[siX])		# Just show bit status.
					myString +=' %4.1d,%4.1d,%d |' % (TouchObjs.FiltValsOfTOs[idx][siX],  TouchObjs.BaseLineValsOfTOs[idx][siX], iLst1[siX])
				os.system('clear')
				print '			Test Procedure for Electrodes'
				print ' 0             1             2             3             4             5             6             7             8             9             10             11'
				print myString

#************************************************************************************************************
		time.sleep(0.2)
except KeyboardInterrupt:							# Required during development.
	print ""
	print "Kennel Model Stopped!"					# Feedback during development.

# End of pMain.py

