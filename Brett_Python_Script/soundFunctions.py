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

electrodes_back = [0x400, 0x401, 0x402, 0x403, 0x404, 0x405, 0x406, 0x407, 0x408, 0x409, 0x40A, 0x40B, 0x500, 0x501, 0x502, 0x503, 0x504, 0x505, 0x506, 0x507, 0x508, 0x509, 0x50A, 0x50B, 0x510, 0x511, 0x512, 0x513, 0x514, 0x515, 0x516, 0x517, 0x518, 0x519, 0x51A, 0x51B, 0x520, 0x521, 0x522, 0x523, 0x524, 0x525, 0x526, 0x527, 0x528, 0x529, 0x52A, 0x52B, 0x530, 0x531, 0x532, 0x533, 0x534, 0x535, 0x536, 0x537, 0x538, 0x539, 0x53A, 0x53B]
scripts_back = ["C", "C", "B", "B", "A", "A", "null", "null", "null", "null", "null", "null", "L", "K", "L", "J", "J", "K", "N", "O", "O", "N", "M", "M", "X", "X", "Z", "Z", "AA", "AA", "W", "V", "V", "X", "X", "W", "F", "E", "F", "D", "D", "E", "I", "I", "H", "H", "G", "G", "S", "S", "U", "T", "U", "U", "Q", "P", "P", "R", "Q", "R"]

def getSoundName( electrodeName):
	try:
		indexOfElecment = electrodes_back.index(int(electrodeName,16))
		value = scripts_back[indexOfElecment]
		return value
	except ValueError:
		print "Touch not on list!"
		return "null"

def playSound(soundName):
	os.system('mpg321 ./audio/'+soundName+'.mp3')

def playSoundFromElectrode(electrodeName):
	playSound(getSoundName(electrodeName))


