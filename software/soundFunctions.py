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

electrodes_name = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xa, 0xb, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x20, 0x21, 0x22, 0x23, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3a, 0x3b, 0x102, 0x103, 0x104, 0x105, 0x106, 0x107, 0x108, 0x109, 0x10a, 0x10b, 0x110, 0x111, 0x112, 0x113, 0x114, 0x115, 0x116, 0x117, 0x118, 0x119, 0x11a, 0x11b, 0x120, 0x121, 0x122, 0x123, 0x124, 0x125, 0x126, 0x130, 0x131, 0x132, 0x133, 0x134, 0x135, 0x136, 0x137, 0x138, 0x139, 0x13a, 0x13b, 0x200, 0x201, 0x202, 0x203, 0x204, 0x205, 0x206, 0x207, 0x208, 0x209, 0x20a, 0x20b, 0x210, 0x211, 0x212, 0x213, 0x214, 0x215, 0x216, 0x217, 0x218, 0x219, 0x21a, 0x21b, 0x220, 0x221, 0x222, 0x223, 0x224, 0x225, 0x226, 0x227, 0x228, 0x229, 0x22a, 0x22b, 0x230, 0x231, 0x232, 0x233, 0x234, 0x235, 0x236, 0x237, 0x238, 0x239, 0x23a, 0x23b, 0x300, 0x301, 0x302, 0x303, 0x304, 0x305, 0x306, 0x307, 0x308, 0x400, 0x401, 0x402, 0x403, 0x404, 0x405, 0x406, 0x407, 0x408, 0x409, 0x40A, 0x500, 0x501, 0x502, 0x503, 0x504, 0x505, 0x506, 0x507, 0x508, 0x509, 0x50A, 0x50B, 0x510, 0x511, 0x512, 0x513, 0x514, 0x515, 0x516, 0x517, 0x518, 0x519, 0x51A, 0x51B, 0x520, 0x521, 0x522, 0x523, 0x524, 0x525, 0x526, 0x527, 0x528, 0x529, 0x52A, 0x52B, 0x530, 0x531, 0x532, 0x533, 0x534, 0x535, 0x536, 0x537, 0x538, 0x539, 0x53A, 0x53B]
scripts_name = ["22", "22", "38", "36", "21", "21", "99", "corr", "corr", "85", "93", "91", "94", "", "90", "92", "87", "95", "95", "88", "33", "33", "30", "45", "30", "41", "39", "40", "44", "35", "corr", "24", "37", "34", "24", "23", "12", "7", "13", "99", "11", "14", "99", "8", "9", "10", "corr", "16", "78", "77", "78", "corr", "77", "6", "15", "78", "79", "corr", "20", "2", "1", "2", "99", "18", "19", "", "", "", "", "", "", "", "", "", "", "", "", "29", "29", "28", "27", "27", "26", "25", "25", "32", "31", "31", "44", "55", "52", "42", "54", "51", "52", "50", "49", "46", "45", "47", "48", "84", "", "76", "97", "97", "70", "57", "70", "98", "69", "74", "75", "73", "56", "68", "59", "58", "98", "72", "67", "60", "43", "53", "43", "81", "82", "80", "82", "80", "81", "81", "80", "81", "C", "C", "B", "B", "A", "A", "DD", "BB", "BB", "BB", "CC", "L", "K", "L", "J", "J", "K", "N", "O", "O", "N", "M", "M", "X", "X", "Z", "Z", "AA", "AA", "W", "V", "V", "X", "X", "W", "F", "E", "F", "D", "D", "E", "I", "I", "H", "H", "G", "G", "S", "S", "U", "T", "U", "U", "Q", "P", "P", "R", "Q", "R"]

def getSoundName( electrodeName):
	try:
		indexOfElecment = electrodes_name.index(int(electrodeName,16))
		value = scripts_name[indexOfElecment]
		return value
	except ValueError:
		print "Touch not on list!"
		return "null"

def playSound(soundName):
	os.system('mpg321  ~/software/audio/'+soundName+'.mp3')

def playSoundFromElectrode(electrodeName):
	playSound(getSoundName(electrodeName))


