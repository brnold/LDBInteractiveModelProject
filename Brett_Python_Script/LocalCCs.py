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
#  
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
#  x	 Edits.																	TBD			2016-0x-xx
#
#
#************************************************************************************************************
# Local electrode charge current settings.
# Address_Subnet
#
LocalCC0_0	=	[0x5F,	13,	11,	14,	12,	13,	14,	13,	13,	0,	0,	0,	0]		# 13
LocalCC1_0	=	[0x5F,	9,	9,	0,	0,	11,	0,	12,	0,	11,	11,	14,	13]		# 5_3_7
LocalCC2_0	=	[0x5F,	13,	13,	14,	11,	0,	0,	0,	0,	0,	0,	0,	0]		# 5_4 
LocalCC3_0	=	[0x5F,	0,	0,	0, 14,	0,	11,	0,	10,	0,	0,	10,	10]		# 2_4
LocalCCSn0	=	[LocalCC0_0, LocalCC1_0, LocalCC2_0, LocalCC3_0]

LocalCC0_1	=	[0x5F,	19,	19,	8,	9,	8,	8,	0,	9,	12,	0,	9,	0]		# 9_15
LocalCC1_1	=	[0x5F,	12,	0,	12,	0,	11,	0,	12,	8,	0,	26,	22,	21]		# 14_15
LocalCC2_1	=	[0x5F,	9,	11,	9,	0,	9,	0,	9,	0,	0,	0,	0,	0]		# 7
LocalCC3_1	=	[0x5F,	0,	0,	0,	11,	0,	0,	12,	11,	0,	12,	9,	8]		# 8_14
LocalCCSn1	=	[LocalCC0_1, LocalCC1_1, LocalCC2_1, LocalCC3_1]

#						0	1	2	3	4	5	6	7	8	9	10	11
#LocalCC0_2	=	[0x5F,	11,	14,	12,	0,	9,	0,	0,	11,	15,	0,	0,	0]		#7-2
#LocalCC0_2	=	[0x5F,	11,	14,	12,	0,	0,	0,	12,	11,	15,	0,	0,	12]		#7-4
#LocalCC0_2	=	[0x5F,	0,	0,	0,	14,	0,	13,	0,	0,	0,	13,	14,	12]		#7-3
#LocalCC0_2	=	[0x5F,	9,	8,	9,	0,	11,	9,	1,	1,	1,	1,	1,	1]		#6-1
LocalCC0_2	=	[0x5F,	0,	0,	0,	14,	0,	13,	0,	0,	0,	13,	14,	12]		#7-1
#LocalCC0_2	=	[0x5F,	1,	1,	1,	1,	40,	1,	1,	1,	1,	1,	1,	1]		# Test the overrides
#LocalCC0_2	=	[0x5F,	9,	11,	9,	11,	0,	0,	11,	0,	11,	0,	0,	0]		# 6_3
#LocalCC0_2	=	[0x5F,	8,	0,	8,	0,	0,	9,	8,	9,	8,	9,	9,	0]		# 3_16
#LocalCC0_2	=	[0x5F,	16,	18,	14,	16,	0,	11,	0,	0,	0,	0,	0,	0]		# 18_19
#LocalCC0_2	=	[0x5F,	9,	9,	9,	0,	9,	0,	0,	9,	0,	0,	0,	11]		# 1_5 
#LocalCC0_2	=	[0x5F,	0,	0,	0, 14,	0,	11,	0,	10,	0,	0,	10,	10]		# 2_4 
#LocalCC0_2	=	[0x5F,	13,	13,	14,	11,	0,	0,	0,	0,	0,	0,	0,	0]		# 5_4 
#LocalCC0_2	=	[0x5F,	9,	9,	0,	0,	11,	0,	12,	0,	11,	11,	14,	13]		# 5_3_7
#LocalCC0_2	=	[0x5F,	9,	11,	9,	0,	9,	0,	9,	0,	0,	0,	0,	0]		# 7
#LocalCC0_2	=	[0x5F,	13,	11,	14,	12,	13,	14,	13,	13,	0,	0,	0,	0]		# 13
#LocalCC0_2	=	[0x5F,	0,	0,	0,	11,	0,	0,	12,	11,	0,	12,	9,	8]		# 8_14
#LocalCC0_2	=	[0x5F,	12,	0,	12,	0,	11,	0,	12,	8,	0,	26,	22,	21]		# 14_15
#LocalCC0_2	=	[0x5F,	19,	19,	8,	9,	8,	8,	0,	9,	12,	0,	9,	0]		# 9_15
#						0	1	2	3	4	5	6	7	8	9	10	11
# LocalCC0_2	=	[0x5F,	14,	0,	9,	0,	0,	8,	8,	8,	0,	9,	0,	0] 

#LocalCC0_2	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC1_2	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC2_2	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC3_2	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCCSn2	=	[LocalCC0_2, LocalCC1_2, LocalCC2_2, LocalCC3_2]

LocalCC0_3	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC1_3	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC2_3	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCC3_3	=	[0x5F,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0] 
LocalCCSn3	=	[LocalCC0_3, LocalCC1_3, LocalCC2_3, LocalCC3_3]

LocalCC0_4	=	[0x5F,	9,	8,	9,	0,	11,	9,	1,	1,	1,	1,	1,	1]		#6-1
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
