#************************************************************************************************************ 
#  ECE 491 Senior Design
#  Winter 2016
#  Team 6 
#
#  Python Script		: Threshold.py
#
#  Purpose: 
#  Provides a list of Threshold register settings for each MPR 121 that can be used 
#  in our touch system. 
#
#  Primary coder																	Benjamin
#  Secondary coder																	Bret
#  Code contributor																	Katrina
#  Code contributor																	Ryan
#************************************************************************************************************ 
#  Revision      
#  0	 Supporting script Threshold settings.										Bret		2016-03-20                     
#  1	 Add setting specific to sections of the floor panels on the                   
#        on the back side of the model.												Bret		2016-04-10
#  2	 Add setting specific to sections of the floor panels on the                   
#        on the back side of the model.												Bret		2016-04-12
#  3	 Label Thresholds for each SparkFun breakout board.							Bret		2016-04-18            
#  4	 Finished setting Thresholds for each SparkFun breakout board.				Bret		2016-04-23            
#
#************************************************************************************************************

# Threshold Settings address 0 subnet 0
# Address_Subnet
#
Threshold0_0	=	[0x41,	35,12,	35,12,	30,9,	24,8,	24,8,	12,6,	12,6,	12,6,	12,6,	12,6,	24,8,	24,8,] # 5_3_7
Threshold1_0	=	[0x41,	35,12,	12,6,	24,8,	30,9,	18,6,	35,12,	30,9,	30,9,	30,9,	12,6,	12,6,	12,6,] # 13
Threshold2_0	=	[0x41,	20,7,	24,8,	12,6,	9,5,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,] # 5_4 
Threshold3_0	=	[0x41,	12,6,	12,6,	25,8,	20,7,	15,7,	15,7,	20,7,	25,8,	15,7,	15,7,	35,12,	12,6,] # 2_4
ThresholdSn0	=	[Threshold0_0, Threshold1_0, Threshold2_0, Threshold3_0]

Threshold0_1 = [0x41,	15,10,	15,10,	25,8,	35,12,	35,6,	35,12,	12,6,	35,12,	25,8,	20,7,	20,7,	12,6] # 9_15
Threshold1_1 = [0x41,	25,8,	12,6,	15,12,	12,6,	12,6,	15,7,	25,8,	22,8,	25,8,	12,6,	12,6,	25,8] # 14_15
Threshold2_1 = [0x41,	35,12,	15,7,	30,9,	25,8,	30,9,	12,6,	30,9,	15,10,	15,10,	15,10,	15,10,	15,10] # 7
Threshold3_1 = [0x41,	15,10,	15,10,	15,10,	15,10,	15,10,	15,10,	15,10,	15,10,	15,10,	15,10,	15,10,	15,10] # 8_14 #This one is not working 4/29
ThresholdSn1 = [Threshold0_1, Threshold1_1, Threshold2_1, Threshold3_1]
#							0		1		2		3		4		5		6		7		8		9		10		11
Threshold0_2 = [0x41,	15,7,	35,12,	15,7,	25,8,	25,8,	25,8,	30,9,	30,9,	12,6,	12,6,	12,6,	12,6]	# 1_5
Threshold1_2 = [0x41,	35,12,	40,15,	20,9,	25,8,	20,7,	35,12,	15,7,	15,7,	15,7,	30,9,	30,9,	12,6]	# 6_3
Threshold2_2 = [0x41,	30,9,	15,10,	15,7,	30,9,	20,7,	12,6,	12,6,	25,8,	15,7,	12,6,	40,20,	40,20]	# 17
Threshold3_2 = [0x41,	20,7,	20,7,	12,6,	15,7,	12,6,	15,7,	20,7,	35,12,	10,4,	30,9,	35,12,	15,7]	# 3_16
ThresholdSn2 = [Threshold0_2, 	Threshold1_2, 	Threshold2_2, Threshold3_2]

Threshold0_3 = [0x41,	15,7,	30,9,	25,8,	15,7,	35,12,	12,6,	30,9,	30,9,	25,8,	15,10,	15,10,	15,10]	# 18_19
Threshold1_3 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6]
Threshold2_3 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6]
Threshold3_3 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6]
ThresholdSn3 = [Threshold0_3, 	Threshold1_3, 	Threshold2_3, Threshold3_3]

Threshold0_4 = [0x41,	40,20,	35,10,	15,8,	35,22,	20,8,	25,12,	10,4,	10,4,	10,4,	10,4,	10,4,	35,10]	# 6-1
Threshold1_4 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6]
Threshold2_4 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6]
Threshold3_4 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6]
ThresholdSn4 = [Threshold0_4, 	Threshold1_4, 	Threshold2_4, Threshold3_4]

Threshold0_5 = [0x41,	17,11,	18,7,	17,11,	20,8,	20,8,	20,10,	17,11,	17,11,	20,8,	20,10,	15,10,	20,8]	# 7-1
Threshold1_5 = [0x41,	20,8,	15,10,	20,10,	15,8,	17,11,	50,35,	20,10,	30,12,	15,10,	17,11,	17,10,	15,8]	# 7-2
Threshold2_5 = [0x41,	30,12,	15,10,	20,10,	15,8,	17,11,	50,35,	25,10,	30,12,	15,10,	17,11,	15,10,	17,11]	# 7-4
Threshold3_5 = [0x41,	17,11,	18,7,	17,11,	20,8,	30,12,	35,10,	18,7,	20,8,	17,11,	35,10,	15,10,	30,12]	# 7-3
ThresholdSn5 = [Threshold0_5, 	Threshold1_5, 	Threshold2_5, Threshold3_5]

Threshold0_6 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,]
Threshold1_6 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,]
Threshold2_6 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,]
Threshold3_6 = [0x41,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,	12,6,]
ThresholdSn6 = [Threshold0_6, 	Threshold1_6, 	Threshold2_6, Threshold3_6]

#							0		1		2		3		4		5		6		7		8		9		10		11
Threshold0_7 = [0x41,	40,10,	18,7,	40,20,	35,10,	30,8,	40,20,	18,7,	40,20,	17,11,	40,15,	20,8,	30,8]
Threshold1_7 = [0x41,	17,11,	18,7,	17,11,	20,8,	20,8,	20,10,	17,11,	17,11,	20,8,	20,10,	15,10,	20,8]
Threshold2_7 = [0x41,	17,11,	18,7,	17,11,	20,8,	20,8,	20,10,	17,11,	17,11,	20,8,	20,10,	15,10,	20,8]
Threshold3_7 = [0x41,	17,11,	18,7,	17,11,	20,8,	20,8,	20,10,	17,11,	17,11,	20,8,	20,10,	15,10,	20,8]	# 7-3
ThresholdSn7 = [Threshold0_7, 	Threshold1_7, 	Threshold2_7, Threshold3_7]
ThresholdAll = [ThresholdSn0, ThresholdSn1, ThresholdSn2, ThresholdSn3, ThresholdSn4, ThresholdSn5, ThresholdSn6, ThresholdSn7]
