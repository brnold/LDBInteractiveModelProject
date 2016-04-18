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
#  0	Created			Benjamin Nold
# 
#************************************************************************************************************

import os

electrodes_back = [0x610, 0x611, 0x612, 0x613, 0x614, 0x615, 0x616, 0x617, 0x618, 0x619, 0x61A, 0x61B, 0x710, 0x711, 0x712, 0x713, 0x714, 0x715, 0x716, 0x717, 0x718, 0x719, 0x71A, 0x71B, 0x720, 0x721, 0x722, 0x723, 0x724, 0x725, 0x726, 0x727, 0x728, 0x729, 0x72A, 0x72B, 0x730, 0x731, 0x732, 0x733, 0x734, 0x735, 0x736, 0x737, 0x738, 0x739, 0x73A, 0x73B, 0x740, 0x741, 0x742, 0x743, 0x744, 0x745, 0x746, 0x747, 0x748, 0x749, 0x74A, 0x74B]
scripts_back = ["C", "C", "B", "C", "A", "A", "null", "null", "null", "null", "null", "null", "L", "K", "L", "J", "J", "K", "N", "O", "O", "N", "M", "M", "X", "X", "Z", "Z", "AA", "AA", "W", "V", "V", "X", "X", "W", "F", "E", "F", "D", "D", "E", "I", "I", "H", "H", "G", "G", "S", "S", "U", "T", "U", "U", "Q", "P", "P", "R", "Q", "R"]

def getSoundName( electrodeName):
	try:
		indexOfElecment = electrodes_back.index(electrodeName)
		value = scripts_back[indexOfElecment]
		return value
	except ValueError:
		print "Touch not on list!"
		return "null"

def playSound(soundName):
	os.system('mpg321 ./audio/'+soundName+'.mp3')

def playSoundFromElectrode(electrodeName):
	playSound(getSoundName(electrodeName))


