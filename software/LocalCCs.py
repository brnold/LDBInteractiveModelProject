#************************************************************************************************************ 
#  ECE 491 Senior Design
#  Winter 2016
#  Team 6 
#
#  Python Script		: LocalCCs.py
#
#  Purpose: 
#  Provides a list of local electrode charge current for each MPR 121 that can be used 
#  in our touch system. 
#
#  Primary coder																Benjamin
#  Secondary coder																Bret
#  Code contributor																Katrina
#  Code contributor																Ryan
#************************************************************************************************************ 
#  Revision      
#  0	 Supporting script local electrode charge current settings.				Bret		2016-03-20
#  1	 Add setting specific to sections of the floor panels on the                   
#        on the back side of the model.											Bret		2016-04-10
#  2	 Add setting specific to sections of the floor panels on the                   
#        on the back side of the model.											Bret		2016-04-12
#
#  3	 Set LocalCCs for each SparkFun breakout board.							Bret		2016-04-18            
#
#  4	 Final LocalCCs edits.													Bret		2016-04-23            
#
#************************************************************************************************************
# Local electrode charge current settings.
# Address_Subnet
#
LocalCC0_0	=	[0x5F,	9,	9,	0,	0,	11,	0,	12,	0,	11,	11,	14,	13]		# 5_3_7
LocalCC1_0	=	[0x5F,	13,	1,	14,	12,	13,	14,	13,	13,	13,	0,	0,	0]		# 13
LocalCC2_0	=	[0x5F,	13,	13,	14,	11,	0,	0,	0,	0,	0,	0,	0,	0]		# 5_4 
LocalCC3_0	=	[0x5F,	0,	0,	0, 14,	0,	11,	0,	10,	0,	0,	10,	10]		# 2_4
LocalCCSn0	=	[LocalCC0_0, LocalCC1_0, LocalCC2_0, LocalCC3_0]

LocalCC0_1	=	[0x5F,	1,	1,	8,	9,	8,	8,	0,	9,	12,	0,	9,	0]		# Floor panel 9_15
LocalCC1_1	=	[0x5F,	14,	12,	13,	13,	15,	11,	13,	10,	12,	15,	15,	15]		# Floor panel 14_15
LocalCC2_1	=	[0x5F,	9,	10,	9,	9,	9,	9,	9,	0,	0,	0,	0,	0]		# Floor panel 7
LocalCC3_1	=	[0x5F,	11,	11,	11,	11,	11,	11,	12,	11,	11,	12,	9,	8]		# Floor panel 8_14
LocalCCSn1	=	[LocalCC0_1, LocalCC1_1, LocalCC2_1, LocalCC3_1]

LocalCC0_2	=	[0x5F,	11,	10, 	11,	11,	0,	11,	0,	11,	14,	14,	14,	14]		# Floor panel 1_5 
LocalCC1_2	=	[0x5F,	9,	11,	9,	11,	0,	0,	11,	0,	11,	0,	0,	0]		# Floor panel 6_3
LocalCC2_2	=	[0x5F,	8,	5,	8,	0,	0,	10,	11,	10,	0,	9,	8,	8]		# Floor panel 17
LocalCC3_2	=	[0x5F,	10,	0,	11,	13,	13,	12,	11,	11,	12,	9,	10,	12]		# Floor panel 3_16
LocalCCSn2	=	[LocalCC0_2, LocalCC1_2, LocalCC2_2, LocalCC3_2]

LocalCC0_3	=	[0x5F,	13,	13,	11,	11,	0,	11,	0,	0,	0,	0,	0,	0]		# Floor panel 18_19
LocalCC1_3	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC2_3	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC3_3	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCCSn3	=	[LocalCC0_3, LocalCC1_3, LocalCC2_3, LocalCC3_3]

LocalCC0_4	=	[0x5F,	9,	8,	9,	0,	11,	9,	18,	18,	17,	18,	18,	0]		#6-1
LocalCC1_4	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC2_4	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC3_4	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCCSn4	=	[LocalCC0_4, LocalCC1_4, LocalCC2_4, LocalCC3_4]

LocalCC0_5	=	[0x5F,	0,	0,	0,	14,	0,	13,	0,	0,	0,	13,	14,	12]		#7-1
LocalCC1_5	=	[0x5F,	11,	14,	12,	0,	9,	0,	0,	11,	15,	0,	0,	0]		#7-2
LocalCC2_5	=	[0x5F,	11,	14,	12,	0,	0,	0,	12,	11,	15,	0,	0,	12]		#7-4
LocalCC3_5	=	[0x5F,	0,	0,	0,	14,	0,	13,	0,	0,	0,	13,	14,	12]		#7-3
LocalCCSn5	=	[LocalCC0_5, LocalCC1_5, LocalCC2_5, LocalCC3_5]

LocalCC0_6	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC1_6	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC2_6	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC3_6	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCCSn6	=	[LocalCC0_6, LocalCC1_6, LocalCC2_6, LocalCC3_6]

LocalCC0_7	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC1_7	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC2_7	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC3_7	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCCSn7	=	[LocalCC0_7, LocalCC1_7, LocalCC2_7, LocalCC3_7]
LocalCCAll	=	[LocalCCSn0, LocalCCSn1, LocalCCSn2, LocalCCSn3, LocalCCSn4, LocalCCSn5, LocalCCSn6, LocalCCSn7]
